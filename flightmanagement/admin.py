from flightmanagement import app
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flightmanagement.models import *
from flask import request, redirect, url_for


class CommonView(ModelView):
    can_view_details = True
    can_export = True
    create_modal = True
    edit_modal = True
    details_modal = True


class AuthenticatedView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated \
                and current_user.user_role == UserRole.ADMIN:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return self.render('admin/login.html')


class UserView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'Mã người dùng',
        'username': 'Tên người dùng',
        'password': 'Mật khẩu',
        'avatar': 'Ảnh đại diện',
        'email': 'Email',
        'active': 'Hoạt động',
        'user_role': 'Quyền'
    }
    column_list = ['username', 'password', 'avatar', 'email', 'active', 'user_role']
    column_searchable_list = ['username', 'email', 'user_role']
    column_filters = ['username', 'email', 'active', 'user_role']
    form_columns = ['username', 'password', 'avatar', 'email', 'active', 'user_role']


class AirportView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'code': 'Mã sân bay',
        'name': 'Tên sân bay',
        'location_id': 'địa chỉ',
        'active': 'Hoạt động'
    }
    column_list = ['id', 'code', 'name', 'location_id', 'active']
    column_searchable_list = ['code', 'name', 'location_id']
    column_filters = ['code', 'active', 'name']
    form_columns = ['code', 'name', 'location_id', 'active']


class PricingView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'code': 'Mã loại giá',
        'name': 'Tên loại giá',
        'percent': 'phần trăm'
    }
    column_list = ['id', 'code', 'name', 'percent']
    column_searchable_list = ['code', 'name', 'percent']
    column_filters = ['code', 'name', 'percent']
    form_columns = ['code', 'name', 'percent']


class TypeOfPositionView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'type_of_position_name': 'Tên loại hạng vé',
        'description': 'Mô tả',
        'percent': 'Chú thích'
    }
    column_list = ['id', 'type_of_position_name', 'description', 'percent']
    column_searchable_list = ['type_of_position_name', 'description']
    column_filters = ['type_of_position_name', 'description']
    form_columns = ['type_of_position_name', 'description', 'percent']


class DiscountView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'code': 'Mã giảm giá',
        'name': 'Tên mã giảm',
        'percent': 'phần trăm'
    }
    column_list = ['id', 'code', 'name', 'percent']
    column_searchable_list = ['code', 'name', 'percent']
    column_filters = ['code', 'name', 'percent']
    form_columns = ['code', 'name', 'percent']


class AirplaneView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'code': 'Mã máy bay',
        'name': 'Tên máy bay',
        'type': 'Loại máy bay',
        'capacity': 'Sức chứa',
        'model_year': 'Năm sản xuất',
        'location_id': 'Sân bay',
        'status': 'Tình trạng',
        'active': 'Hoạt động'
    }
    column_list = ['code', 'name', 'type', 'capacity', 'model_year', 'location_id', 'status', 'active']
    column_searchable_list = ['code', 'name', 'type', 'location_id']
    column_filters = ['code', 'name', 'type', 'location_id']
    form_columns = ['code', 'name', 'type', 'capacity', 'model_year', 'location_id', 'status', 'active']


class FlightView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'code': 'Mã chuyến bay',
        'name': 'Tên chuyến bay',
        'route': 'Hành trình',
        'airplane': 'Máy bay',
        'pilot': 'Phi công',
        'start_time': 'Giờ cất cánh',
        'end_time': 'Giờ hạ cánh',
        'gate': 'Cổng vào',
        'delay': 'Delay',
        'price': 'Giá vé gốc',
        'pricing_id': 'Loại giá'
    }
    column_list = ['code', 'name', 'route', 'airplane', 'pilot', 'start_time', 'end_time', 'gate', 'delay', 'price',
                   'pricing_id']
    column_searchable_list = ['code', 'route', 'airplane', 'start_time', 'end_time']
    column_filters = ['code', 'route', 'airplane', 'start_time', 'end_time']
    form_columns = ['code', 'name', 'route', 'airplane', 'pilot', 'start_time', 'end_time', 'gate', 'delay', 'price',
                    'pricing_id']


class BookingView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'flight_id': 'Mã chuyến bay',
        'booking_date': 'Ngày giờ đặt vé',
        'cccd_cmnd': 'cccd_cmnd',
        'firstname': 'Tên',
        'lastname': 'Họ',
        'gender': 'Giới tính',
        'phone': 'Số điện thoại',
        'date_of_birth': 'Ngày sinh',
        'type_of_position': 'hạng vé',
        'position': 'Số ghế'
    }
    column_list = ['flight_id', 'booking_date', 'cccd_cmnd', 'firstname', 'lastname', 'gender', 'phone',
                   'date_of_birth', 'type_of_position', 'position']
    column_searchable_list = ['flight_id', 'booking_date', 'type_of_position', 'position']
    column_filters = ['flight_id', 'booking_date', 'type_of_position', 'position']
    form_columns = ['flight_id', 'booking_date', 'cccd_cmnd', 'firstname', 'lastname', 'gender', 'phone',
                    'date_of_birth', 'type_of_position', 'position']


class RouteView(CommonView, AuthenticatedView):
    column_labels = {
        'id': 'id',
        'code': 'Mã hành trình',
        'name': 'Tên hành trình',
        'start_location': 'Điểm đi',
        'end_location': 'Điểm đến',
    }
    column_list = ['id', 'code', 'name', 'start_location', 'end_location']
    column_searchable_list = ['id', 'code', 'start_location', 'end_location']
    column_filters = ['code', 'name', 'start_location', 'end_location']
    form_columns = ['code', 'name', 'start_location', 'end_location']


class MyAdminView(AdminIndexView):
    @expose('/', methods=['post', 'get'])
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        if current_user.is_authenticated \
                and current_user.user_role == UserRole.ADMIN:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return self.render('admin/login.html')


admin = Admin(app=app, name='MYCHU ADMIN', template_mode='bootstrap4', index_view=MyAdminView())

admin.add_view(UserView(User, db.session, name='Account'))
admin.add_view(AirportView(Airport, db.session, name='Airport'))
admin.add_view(AirplaneView(Airplane, db.session, name='Airplane'))
admin.add_view(RouteView(Route, db.session, name='Route'))
admin.add_view(FlightView(Flight, db.session, name='Flight'))
admin.add_view(PricingView(Pricing, db.session, name='Pricing'))
admin.add_view(TypeOfPositionView(TypeOfPosition, db.session, name='Class'))
admin.add_view(DiscountView(Discount, db.session, name='Discount'))
admin.add_view(BookingView(Booking, db.session, name='Booking'))
