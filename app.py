# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
"""Thêm một công việc mới vào danh sách."""
tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
# Liệt kê tất cả các công việc, đánh dấu công việc, xóa công việc
tasks = []

def add_task(task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Đã thêm công việc: {task_name}")

def list_tasks():
    print("Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"✅ Đã hoàn thành: {tasks[index]['name']}")
    else:
        print("❌ Không tìm thấy công việc.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"🗑️ Đã xóa công việc: {removed_task['name']}")
    else:
        print("❌ Chỉ số không hợp lệ!")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    add_task("Dọn phòng")

    complete_task(0)
    list_tasks()

    delete_task(1)
    list_tasks()



