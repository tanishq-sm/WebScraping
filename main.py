from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

# ✅ Setup Chrome with custom profile
options = Options()
options.add_argument(r"--user-data-dir=C:\\Users\\VICTUS\\AppData\\Local\\Google\\Chrome\\MySeleniumProfile")
options.add_argument("--start-maximized")
options.add_argument("--log-level=3")  # Suppresses most logs
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# ✅ Launch browser using saved profile
driver = webdriver.Chrome(options=options)

# 🌐 Navigate to the WRIS website
driver.get("https://indiawris.gov.in/dataSet/#/dataSet")
time.sleep(10)

wait = WebDriverWait(driver, 10)



# Select "Ground Water Level"
try:
    dropdown = wait.until(EC.presence_of_element_located((By.ID, "applicationSelect")))
    select = Select(dropdown)
    select.select_by_visible_text("Ground Water Level")
    print("✅ 'Ground Water Level' selected.")
    time.sleep(10)  # Wait after selection
except Exception as e:
    print(f"❌ Error selecting dataset: {e}")

# 2. Select "Admin" from Data Category
try:
    view_select = wait.until(EC.presence_of_element_located((By.ID, "viewSelect")))
    view_select.click()
    select_view = Select(view_select)
    select_view.select_by_visible_text("Admin")
    print("✅ 'Admin' data category selected.")
    time.sleep(5)
except Exception as e:
    print(f"❌ Error selecting view: {e}")

# 3. Select State = "Madhya Pradesh"
wait = WebDriverWait(driver, 3)

try:
    # 1. Click the dropdown button using JS (most reliable)
    dropdown_btn = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "ng-multiselect-dropdown:nth-of-type(1) .dropdown-btn")))
    driver.execute_script("arguments[0].click();", dropdown_btn)
    print("📂 Opened state dropdown.")
    time.sleep(1)

    # 2. Wait for the checkbox input by aria-label
    checkbox_input = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'li.multiselect-item-checkbox input[aria-label="Madhya pradesh"]')))

    # 3. Scroll to and click the checkbox using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_input)
    driver.execute_script("arguments[0].click();", checkbox_input)
    print("✅ 'Madhya pradesh' successfully selected.")
    time.sleep(3)
except Exception as e:
    print(f"❌ Error selecting 'Madhya pradesh': {e}")

# 4. Select District = "Indore"
# Wait for 'Indore' checkbox to appear after state is selected
try:
    # Click the district dropdown
    district_dropdown = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "#selected_district_forDownload .dropdown-btn")))
    driver.execute_script("arguments[0].click();", district_dropdown)
    print("📂 Opened district dropdown.")
    time.sleep(1)  # small delay to let list start loading

    # Wait for 'Indore' to appear (up to 10 seconds)
    ashok_nagar_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
        'li.multiselect-item-checkbox input[aria-label="Ashok nagar"]'))
    )

    # Scroll to and click it
    driver.execute_script("arguments[0].scrollIntoView(true);", ashok_nagar_checkbox)
    driver.execute_script("arguments[0].click();", ashok_nagar_checkbox)
    print("✅ 'Ashok nagar' successfully selected.")
    time.sleep(3)
except TimeoutException:
    print("❌ Timeout: 'Ashok nagar' did not appear in dropdown. Check if district list loaded.")

# Ensure previous district "Ashok nagar" is selected before running this
try:
    # 1. Open the tehsil dropdown
    tehsil_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#selected_tehsil_forDownload .dropdown-btn"))
    )
    driver.execute_script("arguments[0].click();", tehsil_dropdown)
    print("📂 Opened tehsil dropdown.")
    time.sleep(1)

    # 2. Wait for "Essagarh" checkbox to appear
    essagarh_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
        'li.multiselect-item-checkbox input[aria-label="Essagarh"]'))
    )

    # 3. Scroll to and click "Essagarh"
    driver.execute_script("arguments[0].scrollIntoView(true);", essagarh_checkbox)
    driver.execute_script("arguments[0].click();", essagarh_checkbox)
    print("✅ 'Essagarh' tehsil successfully selected.")
    time.sleep(3)

except Exception as e:
    print(f"❌ Error selecting 'Essagarh' tehsil: {e}")
    
# 4. Select Block = "Isagarh"
try:
    block_dropdown_btn = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#selected_block_forDownload .dropdown-btn")))
    
    # ✅ Wait until "Isagarh" appears in the dropdown options
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'li.multiselect-item-checkbox input[aria-label="Isagarh"]')))
    
    driver.execute_script("arguments[0].click();", block_dropdown_btn)
    print("📂 Opened block dropdown.")
    time.sleep(1)
    
    isagarh_block = driver.find_element(By.CSS_SELECTOR, 'li.multiselect-item-checkbox input[aria-label="Isagarh"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", isagarh_block)
    driver.execute_script("arguments[0].click();", isagarh_block)
    print("✅ 'Isagarh' block selected.")
    time.sleep(3)
except TimeoutException:
    print("❌ 'Isagarh' block not found. Wait longer or check for async delay.")

# ✅ After selecting block, wait for agency dropdown to load
try:
    print("⏳ Waiting for agency options to load...")
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'div#agency li.multiselect-item-checkbox input[aria-label="Cgwb"]'
    )))
    print("✅ Agency options loaded.")

    # Now safely open agency dropdown
    agency_dropdown = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'div#agency .dropdown-btn')))
    driver.execute_script("arguments[0].click();", agency_dropdown)
    time.sleep(1)

    # Select CGWB
    cgwb_checkbox = driver.find_element(By.CSS_SELECTOR, 'li.multiselect-item-checkbox input[aria-label="Cgwb"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", cgwb_checkbox)
    driver.execute_script("arguments[0].click();", cgwb_checkbox)
    print("✅ 'Cgwb' agency selected.")
    time.sleep(3)
except TimeoutException:
    print("❌ 'Cgwb' not found in agency dropdown. It may not have loaded correctly.")

from selenium.webdriver.support.ui import Select

try:
    # Wait for the <select> element to be present
    mode_select_element = wait.until(EC.presence_of_element_located((
        By.ID, "manualTelemetry")))

    # Wrap the element with Select class
    select_mode = Select(mode_select_element)

    # Select by visible text "Manual"
    select_mode.select_by_visible_text("Manual")
    print("✅ 'Manual' mode of acquisition selected.")

    time.sleep(1)

except TimeoutException:
    print("❌ Timeout: 'Mode of Acquisition' dropdown not found.")
except Exception as e:
    print(f"❌ Error selecting 'Manual': {e}")

try:
    # Wait for the input box
    start_date_input = wait.until(EC.presence_of_element_located((By.ID, "sDate1")))

    # Option 1 (Preferred): Set value via JavaScript
    driver.execute_script("arguments[0].value = '01/01/1990';", start_date_input)
    print("✅ Start Date set to 1 Jan 1990 using JS.")

    # Optional: If there's an onchange event, trigger it
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", start_date_input)

    time.sleep(3)

except TimeoutException:
    print("❌ Timeout: Could not find Start Date input.")
except Exception as e:
    print(f"❌ Error setting Start Date: {e}")

try:
    # Wait for the end date input field using its ID
    end_date_input = wait.until(EC.presence_of_element_located((By.ID, "eDate1")))

    # Set the value using JavaScript to avoid calendar picker issues
    driver.execute_script("arguments[0].value = '31/05/2025';", end_date_input)

    # Optionally dispatch a change event in case the app needs it to register
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", end_date_input)

    print("✅ End Date set to 31 May 2025.")
    time.sleep(3)

except TimeoutException:
    print("❌ Timeout: End Date input field not found.")
except Exception as e:
    print(f"❌ Error setting End Date: {e}")

try:
    # 1. Open Station Selection dropdown
    station_dropdown = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#dataReport .multiselect-dropdown .dropdown-btn")))
    station_dropdown.click()
    print("📂 Opened Station Selection dropdown.")

    time.sleep(1)  # allow list to populate

    # 2. Select specific station(s), like "Ashoknagar(d)"
    station_label = "Athaikhera"
    station_checkbox = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, f'li.multiselect-item-checkbox input[aria-label="{station_label}"]')))
    
    driver.execute_script("arguments[0].scrollIntoView(true);", station_checkbox)
    driver.execute_script("arguments[0].click();", station_checkbox)
    print(f"✅ Station '{station_label}' selected.")

    time.sleep(3)

except Exception as e:
    print(f"❌ Error during station selection: {e}")

try:
    # Wait until the station dropdown is clickable
    station_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".data-box .dropdown-btn"))
    )

    # Click to close the dropdown
    station_dropdown.click()
    print("✅ Station dropdown closed.")
    time.sleep(6)

except Exception as e:
    print(f"❌ Failed to close station dropdown: {e}")

# Click "Download Metadata" button (second one)
download_meta_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//button[@id='btnSearch'])[2]"))
)
download_meta_btn.click()
print("Clicked Download Metadata button")
time.sleep(10)  # Wait after metadata click

# Wait for modal to be visible
modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
)

# Select the "Student" checkbox
student_checkbox = driver.find_element(By.ID, "Student")
if not student_checkbox.is_selected():
    student_checkbox.click()

# Fill in name and email
driver.find_element(By.ID, "nameID").send_keys("Tanishq")
driver.find_element(By.ID, "emailID").send_keys("tanishq1@gmail.com")

# Click the submit button
submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
submit_btn.click()

print("✅ Modal form submitted successfully.")

# try:
#     # Click the first "Download Data" button
#     download_data_btn = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "(//button[@id='btnSearch'])[1]"))
#     )
#     download_data_btn.click()
#     print("✅ Clicked 'Download Data' button.")

# except Exception as e:
#     print(f"❌ Failed to click 'Download Data': {e}")

import pyautogui
import time

print("⚠ Move your mouse to the 'Save' button within 5 seconds...")
time.sleep(5)

# Get and print the current position of the mouse
x, y = pyautogui.position()
print(f"🖱 Mouse is at position: ({x}, {y})")


# # ⏳ Wait for the download dialog to appear (adjust if needed)
time.sleep(5)

# 🖱 Move to Save button and click
pyautogui.moveTo(743, 556, duration=0.5)
pyautogui.click()

time.sleep(5)

print("✅ Clicked the Save button.")


def select_station(station_label,prev):
    try:
        # Open the station dropdown
        station_dropdown = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#dataReport .multiselect-dropdown .dropdown-btn")))
        station_dropdown.click()
        print("📂 Opened Station Selection dropdown.")

        time.sleep(1)  # Allow list to populate

        # Find and unclick the prev checkbox
        station_checkbox = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, f'li.multiselect-item-checkbox input[aria-label="{prev}"]')))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", station_checkbox)
        driver.execute_script("arguments[0].click();", station_checkbox)
        print(f"✅ Station '{station_label}' unselected.")

        # Find and click the station checkbox
        station_checkbox = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, f'li.multiselect-item-checkbox input[aria-label="{station_label}"]')))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", station_checkbox)
        driver.execute_script("arguments[0].click();", station_checkbox)
        print(f"✅ Station '{station_label}' selected")

        # Click "Download Metadata" button (second one)
        download_meta_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@id='btnSearch'])[2]"))
            )
        download_meta_btn.click()
        print("Clicked Download Metadata button")
        
        # ⏳ Wait for the download dialog to appear (adjust if needed)
        time.sleep(5)

        # 🖱 Move to Save button and click
        pyautogui.moveTo(743, 556, duration=0.5)
        pyautogui.click()
        time.sleep(3)

        

    except Exception as e:
        print(f"❌ Error during station selection for '{station_label}': {e}")

station_list = [
    "Bahadurpur", "Barkheda", "Chanderi(d)","Damdama", "Dhakoni",  "Jhanghar(s)", "Khalilpur", "Mungaoli(s)",
    "Pachlana", "Piprod(s)", "Rati kheda", "Sahrai", "Sankat mochan", "Saraskheri", "Sehpura chak",
    "Semrisahabad", "Shadora", "Shankarpur"
]

prev="Athaikhera"

for station in station_list:
    select_station(station,prev)
    prev=station

