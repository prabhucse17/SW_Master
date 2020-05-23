class Test:

    def Check_test_status(handle):
        while True:
            try:
                url_string = handle.current_url
                print(url_string)
                if re.search(".*id.*runid.*", url_string) is None:
                    print(datetime.datetime.now(), "Test_Still_Not_submitted")
                    time.sleep(5)
                    continue
                test_info = re.search(".*id=(\d+)&runid=(\d+)", url_string)
                print("test_info =", test_info)
                print("Last Test Submitted ID and Run ID = ", test_info.group(1), test_info.group(2))
                break
            except:
                print("Something Went Wrong !! Trying again")
            time.sleep(5)
        while True:
            try:
                if handle.find_element_by_xpath('/html/body/div[3]/md-content/div[1]/div/button[2]').is_displayed():
                    print(datetime.datetime.now(), ": Test Status Failed")
                    print(handle.find_element_by_class_name('page-error-msg vi-accent vi-hue-4').get_attribute('value'))
                    break
                elif handle.find_element_by_xpath("/html/body/div/div[3]/div[5]/div[3]/div[6]/div[2]").is_displayed():
                    print(datetime.datetime.now(), ": Test Status Started")
                    break
            except:
                print("Not Loaded properly, Trying Again")
            time.sleep(5)

    def switchtoframe(handle, framename):
        if framename == "":
            while True:
                print("switching to default")
                try:
                    if handle.switch_to_default_content() is None:
                        print("Switched to Default Frame")
                        return True
                    else:
                        print("sleep and Try again")
                        time.sleep(5)
                except:
                    print("Try Again !! : exception occured while switching to default frame")
                    time.sleep(5)
        else:
            while True:
                print("switching to Frame")
                try:
                    if handle.switch_to_frame(framename) is None:
                        print("Switched to Non Default Frame")
                        return True
                    else:
                        print("sleep and Try again")
                        time.sleep(5)
                except:
                    print("Try Again !! : exception occured while switching to Non default frame")
                    time.sleep(5)

    def find(handle, find_by, find_value, action, text_val):
        try_cnt = 0
        if find_by == 'id':
            print("Finding by ID : ", find_value)
            while True and try_cnt <= 5:
                try_cnt = try_cnt + 1
                print("Try Attempt --> ", try_cnt)
                try:
                    if handle.find_element_by_id(find_value).is_displayed() == True:
                        if action == "click":
                            handle.find_element_by_id(find_value).click()
                            return True
                        elif action == "send":
                            # handle.find_element_by_id(find_value).clear()
                            handle.find_element_by_id(find_value).send_keys(text_val)
                            return True
                        elif action == "clearandsend":
                            while len(handle.find_element_by_id(find_value).get_attribute('value')) != 0:
                                handle.find_element_by_id(find_value).send_keys(Keys.BACKSPACE)
                            handle.find_element_by_id(find_value).clear()
                            time.sleep(1)
                            handle.find_element_by_id(find_value).send_keys(text_val)
                            return True
                    else:
                        print("sleeping")
                        time.sleep(5)
                except:
                    print("exception occured")
                    time.sleep(5)
            print("Breaking")
            # pdb.set_trace()
            print("Unable to Locate", find_value)
            exit()
        if find_by == 'xpath':
            print("Finding by xpath :", find_value)
            while True and try_cnt <= 5:
                print("inside while")
                try_cnt = try_cnt + 1
                print("Try Attempt --> ", try_cnt)
                try:
                    if handle.find_element_by_xpath(find_value).is_displayed() == True:
                        if action == "click":
                            handle.find_element_by_xpath(find_value).click()
                            return True
                        elif action == "send":
                            # handle.find_element_by_xpath(find_value).clear()
                            handle.find_element_by_xpath(find_value).send_keys(text_val)
                            return True
                        elif action == "clearandsend":
                            while len(handle.find_element_by_xpath(find_value).get_attribute('value')) != 0:
                                handle.find_element_by_xpath(find_value).send_keys(Keys.BACKSPACE)
                            time.sleep(1)
                            handle.find_element_by_xpath(find_value).clear()
                            time.sleep(1)
                            handle.find_element_by_xpath(find_value).send_keys(text_val)
                            return True
                    else:
                        print("sleeping")
                        time.sleep(5)
                except:
                    print("exception occured")
                    time.sleep(5)
            print("Breaking")
            print("Unable to Locate", find_value)
            exit()
            # pdb.set_trace()
        if find_by == 'class':
            print("Finding by class :", find_value)
            while True and try_cnt <= 5:
                try_cnt = try_cnt + 1
                print("Try Attempt --> ", try_cnt)
                print("inside while")
                try:
                    if handle.find_element_by_class_name(find_value).is_displayed() == True:
                        if action == "click":
                            handle.find_element_by_class_name(find_value).click()
                            return True
                        elif action == "send":
                            # handle.find_element_by_xpath(find_value).clear()
                            handle.find_element_by_class_name(find_value).send_keys(text_val)
                            return True
                        elif action == "clearandsend":
                            while len(handle.find_element_by_class_name(find_value).get_attribute('value')) != 0:
                                handle.find_element_by_class_name(find_value).send_keys(Keys.BACKSPACE)
                            time.sleep(1)
                            handle.find_element_by_class_name(find_value).send_keys(text_val)
                            return True
                    else:
                        handle.find_element_by_xpath(find_value).clear()
                        print("sleeping")
                        time.sleep(5)
                except:
                    print("exception occured")
                    time.sleep(5)
            print("Breaking")
            print("Unable to Locate", find_value)
            exit()
            # pdb.set_trace()

