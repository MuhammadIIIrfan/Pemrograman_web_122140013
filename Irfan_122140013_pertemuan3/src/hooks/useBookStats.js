import { useContext } from 'react';
import { BookContext } from '../context/BookContext';

export const useBookStats = () => {
  const { books } = useContext(BookContext);
  return {
    owned: books.filter(b => b.status === 'owned').length,
    reading: books.filter(b => b.status === 'reading').length,
    wishlist: books.filter(b => b.status === 'wishlist').length,
  };
};
