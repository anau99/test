
function initializeModals() {
    // Get the modal
    var editorialModal = document.getElementById("myModal");

    // Get the button that opens the modal
    var editorialBtn = document.getElementById("show-modal");

    // Get the <span> element that closes the modal
    var editorialClose = editorialModal.getElementsByClassName("close")[0];

    // Bắt sự kiện click vào nút "Editorial"
    editorialBtn.onclick = function() {
        editorialModal.style.display = 'block';
    };

    // When the user clicks on <span> (x), close the modal
    editorialClose.onclick = function () {
        editorialModal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == editorialModal) {
            editorialModal.style.display = "none";
        }
    };

    // Get the chat modal
    var chatModal = document.getElementById("chatModal");

    // Get the button that opens the chat modal
    var chatBtn = document.getElementById("show-chat");

    // Get the <span> element that closes the chat modal
    var closeChat = chatModal.getElementsByClassName("close")[0];

    // Function to open chat modal
    function openChatModal() {
        chatModal.style.display = "block";
    }

    // Function to close chat modal
    function closeChatModal() {
        chatModal.style.display = "none";
    }

    // Open chat modal when Chat button is clicked
    chatBtn.onclick = function() {
        openChatModal();
    };

    // Close chat modal when close button (x) is clicked
    closeChat.onclick = function() {
        closeChatModal();
    };

    // Close chat modal when user clicks anywhere outside of the chat modal
    window.onclick = function(event) {
        if (event.target == chatModal) {
            closeChatModal();
        }
    };
}

// Initialize the modals when the document is fully loaded
document.addEventListener("DOMContentLoaded", initializeModals);

// JavaScript for handling chat functionality
document.addEventListener("DOMContentLoaded", function() {

    const sendChatBtn = document.getElementById('sendChat');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');

    sendChatBtn.addEventListener('click', async () => {
        const message = chatInput.value;
        if (!message) return;

        appendMessage('user', message);
        chatInput.value = '';

        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        appendMessage('bot', data);

        // Highlight code blocks using highlight.js
        const codeBlocks = document.querySelectorAll('code');
        codeBlocks.forEach((codeBlock) => {
            hljs.highlightBlock(codeBlock);
        });
    });

    // function appendMessage(sender, message) {
    //     const messageElement = document.createElement('div');
    //     messageElement.classList.add('chat-message', sender);
    
    //     // Tạo một thẻ <pre> để chứa mã và áp dụng highlight.js
    //     const codeElement = document.createElement('pre');
    //     const codeBlock = document.createElement('code');
    //     codeBlock.textContent = message;
    //     codeElement.appendChild(codeBlock);
    //     hljs.highlightBlock(codeBlock);
    
    //     messageElement.appendChild(codeElement);
    //     chatMessages.appendChild(messageElement);
    //     chatMessages.scrollTop = chatMessages.scrollHeight;

        
    // }
      hljs.highlightAll();
});


