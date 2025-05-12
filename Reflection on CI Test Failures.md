### 🧠 Reflection on Failing Tests in Smart Library Project

Despite setting up a comprehensive CI pipeline with GitHub Actions, some tests in the Smart Library project continue to fail. These tests primarily target the FastAPI endpoints responsible for book, member, and reservation functionalities.

#### 🔍 Root Cause of Failures

The errors stem from unresolved module imports like `ModuleNotFoundError: No module named 'src'` or issues related to route dependencies not being properly injected. These problems are likely tied to:

* Improper `PYTHONPATH` settings in the test or runtime environment.
* Missing repository or service dependencies not being mocked or initialized during tests.
* Complex application structure that depends on runtime configurations or databases not available in the CI environment.

#### 🛠️ Why Fixing It Was Not Possible (At This Stage)

While I explored several solutions, including setting the `PYTHONPATH` manually, reorganizing imports, and even modifying the test client setup, I was unable to resolve the issues due to the following constraints:

* **Time limitations** before the project submission or CI deadline.
* **Lack of mocking or dependency injection**, which is essential for testing FastAPI services in isolation.
* **Incomplete understanding** of FastAPI’s internal testing requirements for complex route services relying on repositories and databases.

#### 🔚 Conclusion

These test failures highlight the importance of designing modular and testable components from the beginning, especially in layered architectures involving routes, services, and repositories. Given more time and support, I would focus on implementing proper dependency injection, mocking database layers, and ensuring environment consistency across development and CI.

#### Screenshot

![Screenshot (39) 3](https://github.com/user-attachments/assets/ce54b6bf-8cb0-4f07-929d-43030a052a42)
