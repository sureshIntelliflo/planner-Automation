# Pytest-BDD Framework
<h2>Information</h2>
<b>pytest-bdd</b>

pytest-bdd is a plugin for pytest that lets users write tests as Gherkin feature files rather than test functions. Because it integrates with pytest, it can work with any other pytest plugins, such as pytest-html for pretty reports and pytest-xdist for parallel testing. It also uses pytest fixtures for dependency injection.

<b>Pytest markers:</b>

pytest-bdd uses pytest markers as a storage of the tags for the given scenario test, so we can use standard test selection.

Pytest allows to group tests using markers. pytest.mark decorator is used to mark a test function with custom metadata like @pytest.mark.smoke. This is very handy when we want to run only a subset of tests like "smoke tests" to quickly verify if the changes made by the developer not breaking any major functionalities.

<h1>Setup in Windows Os</h1>
<h2>Pre-requisites:</h2>

* Download and install PyCharm Community Edition

* Try Cloning Project using Git URL

* Generate Personal Access Token in Github with gist, read:org and repo scopes

* Pycharm will prompt for Virtual environment (allow creation)

* Download gecko and chrome drivers

* Add driver location to PATH(environment variable)


<h2>Steps for initial run in Windows</h2>
* Login to GitHub using Access Token (not credentials)
* Install Dependencies
* Go to requirements.txt and install required dependencies
* Install Gherkin plugin
* Initiate a test run with Terminal Commands
<h1>Setup in Mac Os</h1>
<h2>Pre-requisites:</h2>

* Python plugin in IntelliJ(navigate to IntelliJ Idea->Preferences->Plugins and Install Python plugin)

* Python 3.7 or higher

* IntelliJ or Pycharm(if available)

* Mac OS

<h2>Dependencies:</h2>
NOTE: To be run in Terminal under project path
* pip install pytest

* pip install pytest-bdd

* pip install selenium

* pip install pytest_base_url

* pip install allure-pytest

In order to export all the dependencies, please run * pip freeze > requirements.txt and this requirement.txt can be used as reference to install all dependencies on Jenkins or any other machines

<h2>Terminal Commands:</h2>

<b>Command to run all the tests on Chrome:</b> 

<code>pytest --browsertype chrome</code>
    
<b>Command to run all the tests on Firefox:</b>

<code>pytest --browsertype firefox</code>

<h2>Coding Guide Lines</h2>

* general variables in camel case or snake case - snakecase with underscore as space: client_services
* underscored in global variables - caps with underscore as space: CLIENT_SERVICES
* Class name should be starting with Capital letter ex. BaseClass
* Every test should have comments
* Method Names should be very descriptive and in lower case. There should be underscore between two words. for ex: select_text_and_delete
* File names should be in lower case and underscore should be present between two words. for ex: test_retirement_goal.py

<code>pytest --browsertype firefox</code>

<b>Running Tests with Specific tags and allure reports </b>

<code>pytest -k "<TAG_Name>" --browsertype chrome --alluredir = OutputReports/</code>

<b>Running Allure reports after above step </b>

<code>allure serve Results/</code>
Note: You need to disconnect VPN in order to see allure report as the port on which allure server is run is being blocked by VPN gateway.


Ex: If you want to run specific tests with tags "login", then here is the command: pytest -k "login" --browsertype chrome

<b>Command to generate Step definitions from Feature File:</b>

<code>pytest-bdd generate tests/features/<Feature_fileName>.feature > tests/step_defs/test_<step_defination_filename>.py</code>


<h2>Jenkins configuration:</h2>

For Jenkins configuration:
1. Download and install Allure reports plugin
2. Configure Allure command line from Global tool configuration(attached screenshot)
3. Use custom workspace and provide the repo path
4. In Build step - command for the job as follows -
    pip install -r ./requirements.txt
    pytest -k "retirementgoalrecommendedallocations" --browsertype firefox --alluredir='OutputReports'
5. In Post-Build actions - configure the path as OutputReports
6. See the job configuration screenshot as below -

Note: We have permissions issue at root /Users/ level and unable to run the jobs from MAC Jenkins. So, the configuration is as per Windows OS and we can use the same once we get new windows OS laptops.

!![post-build-jenkins](https://github.jemstep.com/storage/user/154/files/0c319600-2f1f-11eb-9313-718e84cb1208)
![allure-repot](https://github.jemstep.com/storage/user/154/files/66325b80-2f1f-11eb-8ba5-884805c1a511)
![allure](https://github.jemstep.com/storage/user/154/files/66caf200-2f1f-11eb-953c-295454debdc6)
![build-jenkins](https://github.jemstep.com/storage/user/154/files/67638880-2f1f-11eb-8b72-278e923babc5)
![post-build-jenkins](https://github.jemstep.com/storage/user/154/files/67fc1f00-2f1f-11eb-841d-ecada461ed07)








<h2>References:</h2>
 
https://pypi.org/project/pytest-bdd/


