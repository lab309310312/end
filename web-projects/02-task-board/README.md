# 02 - Task Board App

An interactive client-side task board and productivity tracker with real-time status filtering and persistence.

## Features
- **Task Management:** Create tasks with custom priority levels: *Low*, *Medium*, or *High*.
- **Status Filtering:** Quickly filter tasks by *All*, *Active*, or *Done*.
- **Completion Toggle & Deletion:** One-click task completion checkbox and item removal.
- **Bulk Cleanup:** Clear all completed tasks in one click.
- **Data Persistence:** Automatically synchronizes state with browser `localStorage`.
- **Live Counter:** Dynamically displays active vs completed task statistics.

## Files
- `index.html`: Structure including form input, priority selector, filter buttons, and task list.
- `style.css`: Clean dark-mode inspired theme utilizing CSS variables and priority badge colors.
- `script.js`: State management, rendering pipeline, and `localStorage` integration.

## Usage
Open `index.html` in any web browser.
