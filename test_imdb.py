import pytest
from page.imdb import ImdbPage
from config.config import BasePage as BP



@pytest.mark.usefixtures('chrome_driver')
class Test_IMDB(BP):
    def test_see_results(self):

        self.imdb = ImdbPage(self.driver)

        # enter the name in name field
        self.name_data('Will Smith')

        # enter the brith_date in brith_date field
        self.imdb.birth_date_data('25/09/1968', '25/09/1968')

        self.imdb.scroll_down()

        # enter the birth_day_date  birth_day_date field
        self.imdb.birthday_data('09-25')

        # select Awards & recognition field
        self.imdb.awards_data()

        self.imdb.scroll_down()

        # enter the page_topic in the page_topic field
        self.imdb.page_topic_data("Movies")


        self.imdb.scroll_down()

        # select the gender in the gender field
        self.imdb.gender_id()


        # credits field
        self.imdb.credits('Aladdin')

        self.imdb.scroll_down()

        # result button
        self.imdb.search()

        expected_url = ("https://www.imdb.com/search/name/?name=will%20smith&birth_date=1968-09-25,1968-09-25&birth_monthday=09-25&gender=male&roles=tt6139732")


        assert self.driver.current_url == expected_url, "Somthing Went Wrong"