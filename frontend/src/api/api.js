const API_URL = 'http://127.0.0.1:8000';

export const getAuthors = async () => {
    const response = await fetch(`${API_URL}/authors/`);
    return await response.json();
};

export const getBooks = async () => {
    const response = await fetch(`${API_URL}/books/`);
    return await response.json();
};

export const createAuthor = async (author) => {
    const response = await fetch(`${API_URL}/authors/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(author),
    });
    return await response.json();
};

export const createBook = async (book) => {
    const response = await fetch(`${API_URL}/books/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(book),
    });
    return await response.json();
};
