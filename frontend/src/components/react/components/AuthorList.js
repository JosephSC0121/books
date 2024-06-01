import React, { useState, useEffect } from 'react';
import { getAuthors } from '../api/api';

const AuthorList = () => {
    const [authors, setAuthors] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await getAuthors();
            setAuthors(result);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>Authors</h2>
            <ul>
                {authors.map((author) => (
                    <li key={author.id}>{author.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default AuthorList;
