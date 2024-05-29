import React, { useState, useEffect } from 'react';
import { createBook, getAuthors } from '../api/api';

const BookForm = () => {
    const [title, setTitle] = useState('');
    const [authorId, setAuthorId] = useState('');
    const [authors, setAuthors] = useState([]);

    useEffect(() => {
        const fetchAuthors = async () => {
            const result = await getAuthors();
            setAuthors(result);
        };
        fetchAuthors();
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        await createBook({ title, author_id: authorId });
        setTitle('');
        setAuthorId('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Add Book</h2>
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Book Title"
            />
            <select value={authorId} onChange={(e) => setAuthorId(e.target.value)}>
                <option value="">Select Author</option>
                {authors.map((author) => (
                    <option key={author.id} value={author.id}>
                        {author.name}
                    </option>
                ))}
            </select>
            <button type="submit">Add</button>
        </form>
    );
};

export default BookForm;
