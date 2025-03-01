<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    
    // Recipient email address (change this to your email address)
    $to = "your-email@example.com";
    
    // Subject
    $subject = "New Message from Contact Form";

    // Email content
    $body = "You have received a new message from $name ($email):\n\n$message";

    // Headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "<script>alert('Your message has been sent successfully!'); window.location.href = 'index.html';</script>";
    } else {
        echo "<script>alert('Sorry, something went wrong. Please try again later.'); window.location.href = 'index.html';</script>";
    }
}
?>
