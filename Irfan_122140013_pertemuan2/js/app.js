import { saveToStorage, getFromStorage } from './utils.js';
import { loadTasks } from './data.js';

// Class tugas
class Task {
  constructor(name, date) {
    this.name = name;
    this.date = date;
  }
}

// Tambah tugas
const addTask = () => {
  const name = document.getElementById('taskInput').value;
  const date = document.getElementById('taskDate').value;
  if (!name || !date) return;

  const newTask = new Task(name, date);
  const tasks = getFromStorage('tasks');
  tasks.push(newTask);
  saveToStorage('tasks', tasks);

  loadTasks();
  document.getElementById('taskInput').value = '';
  document.getElementById('taskDate').value = '';
};

// Hapus tugas
window.deleteTask = (index) => {
  const tasks = getFromStorage('tasks');
  tasks.splice(index, 1);
  saveToStorage('tasks', tasks);
  loadTasks();
};

// Simpan catatan
const saveNotes = () => {
  const notes = document.getElementById('notes').value;
  localStorage.setItem('notes', notes);
};

// Event listener
export const setupEvents = () => {
  document.getElementById('addTask').addEventListener('click', addTask);
  document.getElementById('saveNotes').addEventListener('click', saveNotes);
};
