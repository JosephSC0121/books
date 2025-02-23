# Minimalist Library

A sleek and minimalistic library UI built with **Astro**, **React**, and **FastAPI**.

## Features
- Clean and distraction-free user interface
- Backend powered by **FastAPI** for high performance
- Frontend built with **Astro** and **React** for a modern web experience
- Seamless browsing and searching of book collections

## Structure

```plaintext
.  
├── backend/       # FastAPI backend handling book data and search  
│   └── main.py  
├── frontend/      # Astro & React frontend for the library UI  
│   ├── components/  # Reusable UI components  
│   ├── pages/  # Library pages  
│   └── main.tsx  
├── assets/        # Images and static content  
│   ├── covers/  # Book cover images  
│   └── ui_previews/  # UI design snapshots  
```

## Install & Run

### Backend (FastAPI)
```sh
cd backend
uvicorn main:app --reload
```

### Frontend (Astro + React)
```sh
cd frontend
pnpm install
pnpm dev
```

## UI Preview

Here are some snapshots of the interface:

![Screenshot 2025-02-22 213907](https://github.com/user-attachments/assets/3e969362-72e5-4335-86b8-3a4f489ff8c5)


