// Polling the backend every 15 seconds to fetch the latest actions
setInterval(async function() {
    const response = await fetch('/latest-actions');
    const actions = await response.json();
    const actionContainer = document.getElementById('actions');
    actionContainer.innerHTML = '';  // Clear previous content

    actions.forEach(action => {
        let actionText = '';
        if (action.action === "PUSH") {
            actionText = `${action.author} pushed to ${action.to_branch} on ${action.timestamp}`;
        } else if (action.action === "PULL_REQUEST") {
            actionText = `${action.author} submitted a pull request from ${action.from_branch} to ${action.to_branch} on ${action.timestamp}`;
        } else if (action.action === "MERGE") {
            actionText = `${action.author} merged branch ${action.from_branch} to ${action.to_branch} on ${action.timestamp}`;
        }

        const actionElement = document.createElement('p');
        actionElement.textContent = actionText;
        actionContainer.appendChild(actionElement);
    });
}, 15000);
