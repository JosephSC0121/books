import React from 'react';
import AuthorList from './AuthorList';
import BookList from './BookList';
import AuthorForm from './AuthorForm';
import BookForm from './BookForm';

const Author = () => {
    return (
        <div>
            <h1>Library</h1>
            <div style={{ display: 'flex', justifyContent: 'space-around' }}>
                <div>
                    <AuthorForm />
                    <AuthorList />
                </div>
            </div>
        </div>
    );
};

export default Author;
