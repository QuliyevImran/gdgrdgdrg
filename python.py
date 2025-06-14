def log_to_db(user_id, name, job):
    cursor.execute("INSERT INTO recommendations (user_id, name, job) VALUES (?, ?, ?)", (user_id, name, job))
    conn.commit()
    log_to_db(user_id=str(message.from_user.id), name=entered_name, job=generated_job)
