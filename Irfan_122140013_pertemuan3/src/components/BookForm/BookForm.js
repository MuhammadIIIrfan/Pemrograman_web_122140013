import React, { useState, useContext } from 'react';
import PropTypes from 'prop-types';
import { BookContext } from '../../context/BookContext';

const BookForm = ({ initialData = {}, onSubmit }) => {
  const [title, setTitle] = useState(initialData.title || '');
  const [author, setAuthor] = useState(initialData.author || '');
  const [status, setStatus] = useState(initialData.status || 'owned');
  const [error, setError] = useState('');
  const { dispatch } = useContext(BookContext);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim() || !author.trim()) {
      setError('Judul dan penulis harus diisi');
      return;
    }
    const book = {
      id: initialData.id || Date.now(),
      title,
      author,
      status,
    };
    dispatch({ type: initialData.id ? 'UPDATE_BOOK' : 'ADD_BOOK', payload: book });
    onSubmit && onSubmit();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Judul"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        placeholder="Penulis"
        value={author}
        onChange={(e) => setAuthor(e.target.value)}
      />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="owned">Milik</option>
        <option value="reading">Baca</option>
        <option value="wishlist">Ingin Dibeli</option>
      </select>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button type="submit">Simpan</button>
    </form>
  );
};

BookForm.propTypes = {
  initialData: PropTypes.object,
  onSubmit: PropTypes.func,
};

export default BookForm;
