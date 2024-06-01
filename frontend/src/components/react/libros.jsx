import React from 'react';
import AuthorList from './AuthorList';
import BookList from './BookList';
import AuthorForm from './AuthorForm';
import BookForm from './BookForm';

const Books = () => {
    return (
        <div>
            <h1>Library</h1>
            <div style={{ display: 'flex', justifyContent: 'space-around' }}>
                <div>
                    <BookForm />
                    <BookList />
                </div>
            </div>
        </div>
    );
};

export default Books;
