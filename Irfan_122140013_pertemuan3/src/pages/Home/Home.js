import React from 'react';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';

const Home = () => {
  return (
    <div>
      <h1>Daftar Buku</h1>
      <BookForm />
      <BookList />
    </div>
  );
};

export default Home;
