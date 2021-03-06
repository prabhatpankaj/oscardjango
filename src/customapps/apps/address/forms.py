# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from customapps.apps.address.models import UserAddress
from oscar.views.generic import PhoneNumberMixin


class UserAddressForm(PhoneNumberMixin, AbstractAddressForm):
    def __init__(self, user, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        self.instance.user = user

    class Meta:
        model = UserAddress
        fields = [
            'customer_name', 'detail_address','line2','line3', 'line4', 'phone_number',
            'postcode','state','country'
        ]
        exclude = [
            'title', 'first_name', 'last_name',
            'search_text'
        ]
        labels = {
            "line3": u"Landmark",
            "postcode": u"Pincode",
            "state": u"State",
        }
