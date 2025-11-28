# Pradeep SDET Portfolio

Welcome to the **Pradeep SDET Portfolio** repository!  
This is a real-world automation testing framework using **Selenium**, **Python**, and **pytest**.  
It features practical organization, maintainability, and scalability for both beginners and experienced SDETs.

## Project Structure

A typical Python Selenium + pytest automation project should have a clean modular structure for rapid development, reusability, and easy test execution:

```
Pradeep_SDET_Portfolio/
├── tests/                   # All test case files (.py), organized by feature/module
│   ├── test_login.py
│   ├── test_checkout.py
│   └── ...
├── pages/                   # Page Object Model classes
│   ├── login_page.py
│   ├── checkout_page.py
│   └── ...
├── utils/                   # Helper modules/utilities for logging, config, etc.
│   ├── driver_factory.py
│   ├── logger.py
│   ├── config_reader.py
│   └── ...
├── data/                    # Test data files (CSV, JSON, Excel, etc.)
│   ├── users.json
│   └── ...
├── reports/                 # Directory for HTML/Allure reports output
│
├── requirements.txt         # List of Python dependencies
├── pytest.ini               # Pytest configuration file
├── conftest.py              # Pytest fixtures and hooks (optional but recommended)
├── .env                     # Environment variable settings (optional)
├── README.md                # Documentation
└── LICENSE
```

## Folder & File Highlights

- **tests/**: Contains pytest-compatible test scripts. Recommended: Group by feature or module.
- **pages/**: Page Object Model classes for each app page, encapsulating element locators and actions.
- **utils/**: Utility helpers (logging, config reading, webdriver initialization, etc.).
- **data/**: Test data, credentials, configurations in various formats.
- **reports/**: Test execution results, reports artifacts.
- **conftest.py**: Shared pytest fixtures (driver initialization, setup/teardown, etc.).
- **pytest.ini**: Customizes pytest behavior (markers, options).
- **requirements.txt**: Essential libraries (selenium, pytest, etc.).
- **.env**: Environment-specific settings such as URLs or credentials (do not commit secrets).
- **README.md**: Project documentation.

## Technologies Used

- **Python**
- **Selenium WebDriver**
- **pytest**
- **Allure / pytest-html** (for reporting)
- **Page Object Model** architecture

## Getting Started

1. **Clone the repository**
    ```bash
    git clone https://github.com/Pradeepgit-cyber/Pradeep_SDET_Portfolio.git
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run tests**
    ```bash
    pytest
    ```

4. **View reports**
    - Reports will be output to the `reports/` directory

## Contributing

Contributions welcome!  
Please raise an [issue](https://github.com/Pradeepgit-cyber/Pradeep_SDET_Portfolio/issues) or submit a pull request for improvements, new features, or bug fixes.

## License

[MIT License](LICENSE)

---

**Contact**:  
Connect via [GitHub](https://github.com/Pradeepgit-cyber/) for collaboration or professional inquiries.
