import React, { useContext, useState } from 'react';
import { BookContext } from '../../context/BookContext';
import BookForm from '../BookForm/BookForm';

const BookList = () => {
  const { books, dispatch } = useContext(BookContext);
  const [editingBook, setEditingBook] = useState(null);

  const handleDelete = (id) => {
    dispatch({ type: 'DELETE_BOOK', payload: id });
  };

  const filteredBooks = books;

  return (
    <div>
      {filteredBooks.map(book => (
        <div key={book.id}>
          <strong>{book.title}</strong> oleh {book.author} ({book.status})
          <button onClick={() => setEditingBook(book)}>Edit</button>
          <button onClick={() => handleDelete(book.id)}>Hapus</button>
        </div>
      ))}
      {editingBook && (
        <BookForm
          initialData={editingBook}
          onSubmit={() => setEditingBook(null)}
        />
      )}
    </div>
  );
};

export default BookList;
