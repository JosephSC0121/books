import React, { useState, useEffect } from 'react';
import { getBooks } from '../api/api';

const BookList = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await getBooks();
            setBooks(result);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>Books</h2>
            <ul>
                {books.map((book) => (
                    <li key={book.id}>{book.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default BookList;
