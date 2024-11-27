project_overview = """
Building CodeFlo: An AI-Powered SaaS for Code Maintenance and Feature Development

**Overview**
CodeFlo is a SaaS platform designed to help businesses reduce the maintenance costs of existing applications and potentially build new applications using AI. It specifically targets solo developers, small agencies, and organizations that face challenges maintaining legacy applications when the original project team is no longer available. By leveraging AI, CodeFlo aims to automate error fixing, feature development, and improve application stability over time.

**Problem Statement**
Maintaining an application without the original development team can be costly and challenging. It often leads to delays in implementing critical changes, difficulty in finding talent with specialized skills, and long onboarding times. This is particularly painful for small agencies and individual developers, as they end up spending significant time on maintenance instead of building new projects.

**The CodeFlo Solution**
- CodeFlo integrates with GitHub Actions to handle application maintenance by running in the CI/CD pipeline, reducing the need for complex infrastructure and offering better security and code custody.
- It allows developers to set up an AI-supported maintenance environment, which includes support queues, error logging, and testing environments.
- The AI continuously monitors reported errors, user feedback, and automatically works on fixes or feature requests in a test environment to ensure stability.

**How It Works**
1. **Support Queue and Error Logging**: CodeFlo enables applications to have a support queue for users to report issues and a logging system for automated error collection.
2. **AI-Driven Bug Fixing and Feature Development**: The AI monitors the queue and error logs to reproduce issues, attempt fixes, and create pull requests for developer review.
3. **Automated Testing Environment**: CodeFlo creates a baseline environment in GitHub Actions, with the ability to run unit and end-to-end tests to verify the functionality and regression of new changes.
4. **Legacy Application Support**: CodeFlo helps developers maintain legacy systems that often lack support resources, by adding automated error handling and improving test coverage.
5. **New Application Development**: CodeFlo allows users to describe new features or applications, which the AI can start developing from scratch, reducing the workload for developers.

**Implementation Components**
- **Web UI**: For configuration, account setup, project management, and API keys.
- **Backend Service**: To handle accounts, billing, project objectives, and other administrative tasks.
- **GitHub Actions Integration**: CodeFlo operates as a Docker-based GitHub Action that modifies project files, performs error handling, and integrates seamlessly into existing CI/CD pipelines.
- **Bootstrap GitHub Actions Workflow**: Provides a streamlined onboarding process for developers who might not have existing workflows, reducing the setup complexity.

**Ideal User Experience**
- **Ease of Use**: Minimal setup complexity, with templates for different project stacks and a "one-click" deployment approach.
- **Reduced Time Spent on Maintenance**: CodeFlo automatically handles routine tasks, bug fixes, and testing, allowing developers to focus on high-value work.
- **Developer Control**: Users can review AI-generated changes, merge pull requests manually, and control the scope of automated fixes.
- **Metrics and Confidence Building**: Provides metrics that show increased project stability and quality over time, helping developers build confidence and demonstrate their value to clients.

**Potential Revenue Model**
CodeFlo is positioned as a subscription service, with pricing starting at $80 per month per project. The value proposition centers around saving developers significant time in maintenance, allowing them to bill clients for work that would otherwise be non-billable or free up time for new projects.

**Key Implementation Steps**
1. **Documentation Generation**: CodeFlo would first create comprehensive documentation of the codebase, mapping features and dependencies to aid future changes.
2. **Test Environment Setup**: Automatically set up an environment for running tests within GitHub Actions, including unit and end-to-end tests.
3. **Test Coverage Improvements**: Evaluate existing test coverage, create tests where needed, and integrate coverage into the CI/CD pipeline.
4. **Refactoring for Maintainability**: Refactor code to improve readability, maintainability, and security, backed by automated testing.
5. **Error Handling and Bug Fixing**: Implement automated error logging and reporting. AI will reproduce bugs, suggest fixes, and open pull requests with proposed changes.
6. **Feature Development**: Allow developers to submit feature ideas, which the AI will attempt to build and provide for review.

**User Pain Addressed**
- CodeFlo helps developers minimize the need for manual testing and bug fixing, which are time-consuming and distracting.
- It reduces task switching, allowing developers to stay focused on current projects without being interrupted by previous client maintenance work.
- CodeFlo provides a solution for legacy systems that are often decommissioned due to the lack of support teams.


"""

opening_summary = """
    **We're (our small team) working on something that we've started using to handle our most hated tasks and we want to know if you think this would help you.** 

    **At a high level**
    Here's what we are using Codeflo for and what we think it can help you with:

    1. Creating and updating documentation for your code (we ALL hate writing docs)
    2. Setting up an maintaining CI/CD testing pipelines (this can feel so optional on a lot of projects)
    3. Building unit tests and e2e tests (we've all been there, no time to write tests, just push to prod, the client is waiting)
    4. Code cleanup and refactoring (If it's not broken, don't fix it right? Until you have to untangle the spaghetti)
    5. Error logging… (what's error logging precious?) 
    6. Automatic bug fixing
    7. New feature development 
"""

opening_call_to_action = """
    **Tell me about the tasks you hate doing the most.**
    **What tasks do you wish you could start doing?**
    **What is the most important goal for you related to your work that you feel like you are not able to achieve?**
    
    This doesn't have to be related to CodeFlo, just tell me about your work and what you wish you could change.
"""