---
name: User story
about: Suggest an idea for this project
title: As <role>, I want <something> so that <something>
labels: 'status: new issue, type: user story'
assignees: ''

---

## Acceptance Criteria

| Given | When | Then |
| :--- | :--- | :--- |
| A user has created a todo | The user adds a due date to the todo | The due date is saved and displayed with the todo |
| A todo has a due date | The current date is past the due date | The todo is visually marked as overdue |
| A user views the todo list | Todos have due dates | Todos are sorted by due date |

---

## Subtasks
- [x] Define how a due date is represented in a todo (data model)
- [ ] Extend the user interface to allow entering a due date
- [ ] Display the due date next to each todo
- [ ] Add visual feedback for overdue todos

---

## Further Information
- Due dates should be optional so existing todos remain valid  
- The feature should not break existing functionality  
- Visual indicators for overdue todos should be clearly distinguishable but not intrusive
