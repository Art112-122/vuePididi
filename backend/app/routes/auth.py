import sqlite3
import smtplib
import random

from flask import render_template, request,  session, jsonify, response
from flask_login import login_user

from connection import get_db_connection
from app import app, login_manager
from ..models import User

users_db = {}




@app.get("/{str:token}/")
def token ():
    return jsonify(response=True), 201 


@app.post("/signup/")
def post_signup():
    username = request.form["username"].strip()
    password = request.form["password"].strip()
    gmail = request.form["gmail"].strip()

    if not all([username, password, gmail]):
        return jsonify(response-True, error_message="All fields are required"), 400

    if len(username) < 3 or len(username) > 20:
        return jsonify(response-True, error_message="Username must be between 3 and 20 characters"), 400

    if not gmail.endswith('@gmail.com'):
        return jsonify(response-True, error_message="Please enter a valid Gmail address"), 400

    if len(password) < 5:
        return jsonify(response-True, error_message="Password must be at least 6 characters long"), 400

    conn = get_db_connection()
    curs = conn.cursor()
    curs.execute("SELECT * FROM users WHERE username = ? OR gmail = ?", (username, gmail))
    existing_user = curs.fetchone()

    if existing_user:
        conn.close()
        if existing_user[1] == username:
            return jsonify(response-True, error_message="Username already exists"), 401
        else:
            return jsonify(response-True, error_message="Email already registered"), 401
    try:
        curs.execute("INSERT INTO users (username, gmail, password, email_verified) VALUES (?, ?, ?, 0)",
                     (username, gmail, password))
        conn.commit()
        user_id = curs.lastrowid

        curs.execute("""INSERT INTO card_info (card_id, first_name, second_name, card_number, cvv_cod, tame_date) 
                       VALUES (?, ?, ?, ?, ?, ?, 0)""",
                     (user_id, "", ""))
        conn.commit()

        user = User(user_id=user_id, username=username, gmail=gmail, password=password, email_verified=False)
        login_user(user)
        session['user_id'] = user_id
        verification_code = generate_verification_code()
        send_email(to_addrs=gmail, code=verification_code)
        session['verification_code'] = verification_code

    except sqlite3.IntegrityError:
        print("Error: Integrity constraint violated.")
        return jsonify(response-True, error_message="Email already registered"), 404
    except sqlite3.Error as error:
        print("Error", error)
        return jsonify(response-True, error_message="Database error occurred"), 404
    finally:
        conn.close()


def send_email(to_addrs, code):
    from_addrs = "vuebank@gmail.com"
    subject = "Welcome to Our Service. That's your security code:"
    body = f"Thank you for signing up! Your verification code is: {code}"
    message = f"From: {from_addrs}\nTo: {to_addrs}\nSubject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_addrs, "tvko chtq awmb dttp")
        server.sendmail(from_addrs, to_addrs, message)
        server.quit()
    except Exception as e:
        print("Error sending email:", e)


@app.post("/verify_code/")
def post_verify_code():
    entered_code = request.form["verification_code"]
    correct_code = session.get('verification_code')
    user_id = session.get('user_id')

    print(f"Debug info:")
    print(f"Entered code: {entered_code}")
    print(f"Correct code: {correct_code}")
    print(f"User ID from session: {user_id}")

    if entered_code == correct_code and user_id:
        conn = get_db_connection()
        curs = conn.cursor()
        try:
            curs.execute("UPDATE users SET email_verified = 1 WHERE user_id = ?", (user_id,))
            affected_rows = curs.rowcount
            conn.commit()
            print(f"Rows affected by update: {affected_rows}")
            print(f"Update successful for user_id: {user_id}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

        session.pop('verification_code', None)
        session.pop('user_id', None)
        return 
    else:
        print(f"Verification failed:")
        print(f"Code match: {entered_code == correct_code}")
        print(f"User ID exists: {user_id is not None}")
        return jsonify(response=True, error_message="Incorrect verification code. Please try again."), 404


def send_mail(to_addrs, code):
    from_addrs = "hktnadm@gmail.com"
    subject = "Welcome to Our Service. That's your security code:"
    body = f"Thank you for signing up! Your verification code is: {code}"
    message = f"From: {from_addrs}\nTo: {to_addrs}\nSubject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_addrs, "tvko chtq awmb dttp")
        server.sendmail(from_addrs, to_addrs, message)
        server.quit()
    except Exception as e:
        print("Error sending email:", e)


def generate_verification_code(length=6):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))




