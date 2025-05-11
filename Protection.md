## 🛡️ Branch Protection Rules for `main`

To ensure code quality, team collaboration, and CI/CD integrity, the `main` branch of this project is protected with the following rules:

### ✅ Enforced Rules & Why They Matter

| Rule                                       | Description                                                                            | Why It Matters                                                                             |
| ------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Require PR Reviews**                     | All changes must go through a Pull Request and be approved by at least **1 reviewer**. | Promotes collaboration and ensures that code is peer-reviewed for quality and consistency. |
| **Require Status Checks to Pass**          | PRs must pass all GitHub Actions (CI tests) before they can be merged.                 | Prevents untested or broken code from entering the production branch.                      |
| **Require Branch Up-to-Date Before Merge** | PRs must be synced with the latest `main` branch before merging.                       | Ensures compatibility and avoids post-merge conflicts.                                     |
| **Restrict Direct Pushes**                 | Direct pushes to `main` are not allowed.                                               | Enforces the use of PRs and CI checks for every change.                                    |
| **Dismiss Stale Approvals**                | If new commits are pushed to a PR, existing approvals are reset.                       | Guarantees the final version of code has been reviewed.                                    |
| **(Optional)** Require Linear History      | Enforces rebase/merge squash strategy (no merge commits).                              | Keeps the commit history clean and easier to navigate.                                     |

> 🔒 These rules are configured under **Settings → Branches → Branch Protection Rules** on GitHub.

---


### 📌 Screenshots

![Screenshot (37)](https://github.com/user-attachments/assets/448e7a7e-e61c-4b93-9382-9c81467b6a48)
![Screenshot (34)](https://github.com/user-attachments/assets/f86324cc-1ea2-4bfa-89ad-f97ff2cba787)
![Screenshot (35)](https://github.com/user-attachments/assets/d732269c-b34d-4c9f-b489-14bc3d3af4dd)
![Screenshot (36)](https://github.com/user-attachments/assets/eb94d5ff-2139-4c17-8bb1-954fc4d7e9cb)


### 📌 Summary

These branch protection settings help:

* Maintain **stable, tested code** on `main`
* Enforce **automated CI/CD pipelines**
* Prevent regressions and production bugs
* Promote a **collaborative development workflow**

