const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/userdb', { useNewUrlParser: true, useUnifiedTopology: true });

// Define User Schema
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  age: Number
});

const User = mongoose.model('User', userSchema);

// Function to insert a new user
async function insertUser(userData) {
  try {
    const newUser = new User(userData);
    await newUser.save();
    console.log('User inserted successfully');
  } catch (error) {
    console.error('Error inserting user:', error);
  } finally {
    mongoose.connection.close();
  }
}

// Example usage
insertUser({ name: 'John Doe', email: 'john@example.com', age: 30 });