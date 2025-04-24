import React from 'react';
import PropTypes from 'prop-types';

const BookFilter = ({ statusFilter, onChange }) => {
  return (
    <select value={statusFilter} onChange={(e) => onChange(e.target.value)}>
      <option value="">Semua</option>
      <option value="owned">Milik</option>
      <option value="reading">Baca</option>
      <option value="wishlist">Ingin Dibeli</option>
    </select>
  );
};

BookFilter.propTypes = {
  statusFilter: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default BookFilter;
