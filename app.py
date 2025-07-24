#gradio wala
import gradio as gr
import requests

# Replace with your actual backend URL (use "http://localhost:5000" if testing locally)
BACKEND_URL = "http://localhost:5000"

def view_data():
    response = requests.get(f"{BACKEND_URL}/get_data")
    if response.ok:
        data = response.json()
        return "\n".join([f"{item['id']}: {item['name']} - {item['email']}" for item in data])
    else:
        return "Failed to fetch data."

def add_data(name, email):
    response = requests.post(f"{BACKEND_URL}/add_data", json={"name": name, "email": email})
    if response.ok:
        return "User added successfully."
    return "Failed to add user."

def update_data(user_id, name, email):
    response = requests.put(f"{BACKEND_URL}/update_data/{user_id}", json={"name": name, "email": email})
    if response.ok:
        return "User updated successfully."
    return "Failed to update user."

def delete_data(user_id):
    response = requests.delete(f"{BACKEND_URL}/delete_data/{user_id}")
    if response.ok:
        return "User deleted successfully."
    return "Failed to delete user."


with gr.Blocks() as demo:
    gr.Markdown("## 🧾 User Management Dashboard (Flask + Gradio)")

    with gr.Tab("View Users"):
        view_output = gr.Textbox(label="Current Users", lines=10)
        view_btn = gr.Button("Refresh Users")
        view_btn.click(fn=view_data, outputs=view_output)

    with gr.Tab("Add User"):
        name = gr.Textbox(label="Name")
        email = gr.Textbox(label="Email")
        add_btn = gr.Button("Add")
        add_output = gr.Textbox(label="Status")
        add_btn.click(fn=add_data, inputs=[name, email], outputs=add_output)

    with gr.Tab("Update User"):
        uid = gr.Number(label="User ID")
        new_name = gr.Textbox(label="New Name")
        new_email = gr.Textbox(label="New Email")
        update_btn = gr.Button("Update")
        update_output = gr.Textbox(label="Status")
        update_btn.click(fn=update_data, inputs=[uid, new_name, new_email], outputs=update_output)

    with gr.Tab("Delete User"):
        delete_id = gr.Number(label="User ID")
        delete_btn = gr.Button("Delete")
        delete_output = gr.Textbox(label="Status")
        delete_btn.click(fn=delete_data, inputs=delete_id, outputs=delete_output)

demo.launch()

