const express = require('express');
const app = express();
const cors = require('cors');
const PORT = 3000;

app.use(cors());

// Handle the root route
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Keep the /users route
app.get('/users', (req, res) => {
  const users = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Smith' },
    { id: 3, name: 'Bob Johnson' }
  ];
  res.json(users);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});