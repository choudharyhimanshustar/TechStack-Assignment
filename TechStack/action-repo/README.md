# Action Repo

This repository is used to trigger GitHub actions like Push, Pull Request, and Merge. These actions are captured by the `webhook-repo` to store details in MongoDB and reflect them in the UI.

## Usage

1. **Push**: Make a change in the code and push it to the remote repository.
2. **Pull Request**: Create a pull request from one branch to another.
3. **Merge**: Merge the branches to complete the workflow.

All these actions will trigger the webhook registered in the `webhook-repo`.
