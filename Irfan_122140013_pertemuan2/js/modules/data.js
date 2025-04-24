// Fungsi untuk render template tugas
export const renderTask = (task, index) => {
    return `
      <li>
        ${task.name} (Deadline: ${task.date})
        <button onclick="deleteTask(${index})">Hapus</button>
      </li>
    `;
  };
  
  // Load data dari localStorage
  export const loadTasks = () => {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = tasks.map((task, i) => renderTask(task, i)).join('');
  };
  
  // Load catatan
  export const loadNotes = () => {
    const savedNotes = localStorage.getItem('notes');
    if (savedNotes) {
      document.getElementById('notes').value = savedNotes;
    }
  };
  