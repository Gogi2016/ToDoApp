# Branch Protection Rules Justification

The following rules are applied to the `main` branch:

- **Require PR reviews**: Ensures code is reviewed and approved before merging to maintain code quality.
- **Require status checks**: Prevents merging if tests fail, ensuring functional stability.
- **Disable direct pushes**: Forces changes to go through a review process.
- **Keeps history clean** and helps teams follow best practices for collaboration and CI/CD.

These rules align with industry standards and help avoid bugs reaching production.
