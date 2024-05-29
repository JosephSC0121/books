import React, { useState } from 'react';
import { createAuthor } from '../api/api';

const AuthorForm = () => {
    const [name, setName] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        await createAuthor({ name });
        setName('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Add Author</h2>
            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Author Name"
            />
            <button type="submit">Add</button>
        </form>
    );
};

export default AuthorForm;
