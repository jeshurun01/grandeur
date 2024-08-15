document.addEventListener('DOMContentLoaded', function() {
    const notificationsContainer = document.getElementById('notifications');

    function displayPosts() {
        const posts = JSON.parse(localStorage.getItem('posts')) || [];

        notificationsContainer.innerHTML = ''; // Réinitialiser les notifications

        posts.sort((a, b) => new Date(b.time) - new Date(a.time)); // Tri par date décroissante

        posts.forEach(post => {
            const notificationElement = document.createElement('div');
            notificationElement.className = 'notification';

            const timeElement = document.createElement('time');
            timeElement.textContent = new Date(post.time).toLocaleString();
            notificationElement.appendChild(timeElement);

            if (post.photo) {
                const img = document.createElement('img');
                img.src = post.photo;
                notificationElement.appendChild(img);
            }

            const messageElement = document.createElement('p');
            messageElement.textContent = post.message;
            notificationElement.appendChild(messageElement);

            notificationsContainer.appendChild(notificationElement);
        });
    }

    displayPosts();
});
