import { loadTasks, loadNotes } from './modules/data.js';
import { setupEvents } from './modules/app.js';

// Inisialisasi awal
document.addEventListener('DOMContentLoaded', () => {
  loadTasks();
  loadNotes();
  setupEvents();
});
