import allure
import logging
import time
import json

def expect_handle(func):
    def _expect_handle(*args, **kwargs):
        for retry_times in range(3):
            try:
                res_params = {
                    "method": args[1],
                    "url": args[2],
                    **kwargs
                }
                allure.attach(bytes('{}'.format(res_params), 'utf-8'), name=f"请求参数_{time.ctime()}",
                              attachment_type=allure.attachment_type.JSON)

                logging.debug(f"接口请求参数: {json.dumps(res_params)}")

                res = func(*args, **kwargs)
                if res.status_code == 200:
                    allure.attach(bytes('{}'.format(res.json()), 'utf-8'), name=f"接口响应_{time.ctime()}",
                                  attachment_type=allure.attachment_type.JSON)

                    logging.debug(f"接口返回参数{json.dumps(res.json())}")
                    return res.json()

                else:
                    logging.warning(f'-> Requests status code error: {res.status_code}')
                    logging.warning(f'>> Retry time: {retry_times + 1}, Wait 2s')
                    time.sleep(2)

            except TimeoutError:
                logging.warning(f'-> Requests timeout 60s')
                logging.warning(f'>> Retry time: {retry_times + 1}, Wait 5s')
                time.sleep(5)

            except Exception as e:
                logging.error(f'-> Requests error: {e}, {e.__class__.__name__}')
                raise e

        return None

    return _expect_handle