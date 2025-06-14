# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import SignupSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from main.serializers import SignupSerializer
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.template.loader import render_to_string  # Optional if using template rendering


# # class SignupWithDogView(APIView):
# #     def post(self, request):
# #         serializer = SignupSerializer(data=request.data)
# #         if serializer.is_valid():
# #             result = serializer.save()
# #             return Response(result, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SignupWithDogView(APIView):
#     def post(self, request):
#         serializer = SignupSerializer(data=request.data)
#         if serializer.is_valid():
#             result = serializer.save()

#             # ✅ Send welcome email
#             user_email = result["user"]["email"]
#             user_name = user_email.split("@")[0].capitalize()

#             html_content = f"""
#                 <div style="font-family:Arial,sans-serif;padding:20px;background:#f9f9f9;">
#                     <h2 style="color:#4CAF50;">Welcome to BarkBox, {user_name}!</h2>
#                     <p>Thanks for signing up. We’re excited to send goodies your dog will love 🐶</p>
#                     <p>Explore your dashboard and update your preferences anytime.</p>
#                     <p style="margin-top:30px;">Cheers,<br/>The BarkBox Team</p>
#                 </div>
#             """

#             try:
#                 email = EmailMessage(
#                     subject="🎉 Welcome to BarkBox!",
#                     body=html_content,
#                     from_email=settings.DEFAULT_FROM_EMAIL,
#                     to=[user_email],
#                 )
#                 email.content_subtype = "html"
#                 email.send()
#             except Exception as e:
#                 print(f"❌ Failed to send welcome email: {e}")

#             return Response(result, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import OrderSerializer

# class OrderCheckoutView(APIView):
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             order = serializer.save()
#             return Response({'order_id': order.id, 'message': 'Order placed successfully'}, status=201)
#         return Response(serializer.errors, status=400)


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from .serializers import UserProfileSerializer, DogSerializer

# class UserProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserProfileSerializer(request.user)
#         return Response(serializer.data)

#     def put(self, request):
#         serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DogProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         dog = getattr(request.user, "dog", None)
#         if dog:
#             serializer = DogSerializer(dog)
#             return Response(serializer.data)
#         return Response({"detail": "Dog profile not found."}, status=404)

#     def put(self, request):
#         dog = getattr(request.user, "dog", None)
#         if not dog:
#             return Response({"detail": "Dog profile not found."}, status=404)
#         serializer = DogSerializer(dog, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.mail import EmailMessage
# from django.conf import settings
# from rest_framework.permissions import AllowAny

# class SendEmailAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         to_email = request.data.get('to')
#         subject = request.data.get('subject')
#         html_content = request.data.get('html')

#         print("📩 Email Request Received:")
#         print("To:", to_email)
#         print("Subject:", subject)
#         print("HTML snippet:", html_content[:100])  # just log the first 100 chars

#         if not all([to_email, subject, html_content]):
#             return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             email = EmailMessage(
#                 subject,
#                 html_content,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [to_email],
#             )
#             email.content_subtype = "html"
#             email.send()
#             return Response({'message': 'Email sent'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status as drf_status
# from .models import Order
# from django.core.mail import EmailMessage
# from django.conf import settings

# class UpdateOrderStatusView(APIView):
#     def post(self, request, order_id):
#         new_status = request.data.get("status")

#         if new_status not in dict(Order.STATUS_CHOICES):
#             return Response({"error": "Invalid status."}, status=400)

#         try:
#             order = Order.objects.get(id=order_id)
#             order.status = new_status
#             order.save()

#             # Send status update email
#             email = EmailMessage(
#                 subject=f"BarkBox Order Update: {new_status.replace('_', ' ').title()}",
#                 body=f"Hi {order.first_name},\n\nYour BarkBox order is now: {new_status.replace('_', ' ').title()} 🐾\n\nThanks for being with us!\n\nBarkBox Team",
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[order.email],
#             )
#             email.send()

#             return Response({"message": f"Order status updated to {new_status}"}, status=200)
#         except Order.DoesNotExist:
#             return Response({"error": "Order not found."}, status=404)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, OrderSerializer, UserProfileSerializer, DogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Order
from datetime import date
from django.contrib.auth import get_user_model




class SignupWithDogView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()

            user_email = result["user"]["email"]
            user_name = user_email.split("@")[0].capitalize()

            html_content = f"""
                <div style="font-family:Arial,sans-serif;padding:20px;background:#f9f9f9;">
                    <h2 style="color:#4CAF50;">Welcome to BarkBox, {user_name}!</h2>
                    <p>Thanks for signing up. We’re excited to send goodies your dog will love 🐶</p>
                    <p>Explore your dashboard and update your preferences anytime.</p>
                    <p style="margin-top:30px;">Cheers,<br/>The BarkBox Team</p>
                </div>
            """

            try:
                email = EmailMessage(
                    subject="🎉 Welcome to BarkBox!",
                    body=html_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[user_email],
                )
                email.content_subtype = "html"
                email.send()
            except Exception as e:
                print(f"❌ Failed to send welcome email: {e}")

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class OrderCheckoutView(APIView):
#     def post(self, request):
#         from .models import MonthlyBox
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             today = date.today()
#             try:
#                 box = MonthlyBox.objects.get(month=today.month, year=today.year)
#             except MonthlyBox.DoesNotExist:
#                 return Response({'error': 'No MonthlyBox defined for this month'}, status=400)

#             order = serializer.save()
#             order.monthly_box = box
#             order.save()

#             return Response({'order_id': order.id, 'message': 'Order placed successfully'}, status=201)
#         return Response(serializer.errors, status=400)

from datetime import timedelta
from dateutil.relativedelta import relativedelta 
User = get_user_model()

class OrderCheckoutView(APIView):
    def post(self, request):
        from .models import MonthlyBox
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.validated_data['email']).first()
            if not user:
                return Response({'error': 'User not found'}, status=404)

            # First box date logic (1 month after signup)
            first_box_date = user.date_joined.date() + relativedelta(months=1)
            today = date.today()

            try:
                box = MonthlyBox.objects.get(month=today.month, year=today.year)
            except MonthlyBox.DoesNotExist:
                return Response({'error': 'No MonthlyBox defined for this month'}, status=400)

            order = serializer.save()
            order.monthly_box = box
            order.total_treats_delivered = 2
            order.total_toys_delivered = 3
            order.created_at = first_box_date  # delay order creation to match first delivery logic
            order.save()

            return Response({'order_id': order.id, 'message': 'Order placed successfully'}, status=201)

        return Response(serializer.errors, status=400)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dog = getattr(request.user, "dog", None)
        if dog:
            serializer = DogSerializer(dog)
            return Response(serializer.data)
        return Response({"detail": "Dog profile not found."}, status=404)

    def put(self, request):
        dog = getattr(request.user, "dog", None)
        if not dog:
            return Response({"detail": "Dog profile not found."}, status=404)
        serializer = DogSerializer(dog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SendEmailAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        to_email = request.data.get('to')
        subject = request.data.get('subject')
        html_content = request.data.get('html')

        print("📩 Email Request Received:")
        print("To:", to_email)
        print("Subject:", subject)
        print("HTML snippet:", html_content[:100])

        if not all([to_email, subject, html_content]):
            return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            email = EmailMessage(
                subject,
                html_content,
                settings.DEFAULT_FROM_EMAIL,
                [to_email],
            )
            email.content_subtype = "html"
            email.send()
            return Response({'message': 'Email sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class UpdateOrderStatusView(APIView):
#     def post(self, request, order_id):
#         new_status = request.data.get("status")

#         if new_status not in dict(Order.STATUS_CHOICES):
#             return Response({"error": "Invalid status."}, status=400)

#         try:
#             order = Order.objects.get(id=order_id)
#             order.status = new_status
#             order.save()

#             status_text = new_status.replace('_', ' ').title()

#             html_content = f"""
#                 <div style="font-family: Arial, sans-serif; background: #f9f9f9; padding: 30px; border-radius: 10px; max-width: 600px; margin: auto; color: #333;">
#                   <h2 style="color: #4CAF50;">🐾 Hi {order.first_name},</h2>

#                   <p style="font-size: 16px;">
#                     We wanted to give you a quick update — your BarkBox order is now marked as:
#                     <strong style="color: #4CAF50;">{status_text}</strong> 🎉
#                   </p>

#                   <p style="font-size: 16px;">
#                     Our team is preparing everything to ensure your pup gets the best treats, toys, and tail-wagging joy 💌.
#                   </p>

#                   <div style="background: #fff; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 0 8px rgba(0,0,0,0.05);">
#                     <h3 style="margin-bottom: 10px;">📦 Order Details:</h3>
#                     <ul style="padding-left: 20px; font-size: 15px;">
#                       <li><strong>Plan:</strong> {order.get_selected_plan_display()}</li>
#                       <li><strong>Shipping To:</strong> {order.address}, {order.city}, {order.state}, {order.zip}</li>
#                       <li><strong>Status:</strong> {status_text}</li>
#                     </ul>
#                   </div>

#                   <p style="font-size: 15px;">Stay tuned — we’ll keep you posted on every step until your box arrives at your doorstep 🐶📬</p>

#                   <p style="margin-top: 30px; font-size: 15px;">
#                     Woofs & Wags,<br/>
#                     <strong>The BarkBox Team</strong> 💙
#                   </p>
#                 </div>
#             """

#             email = EmailMessage(
#                 subject=f"📦 BarkBox Order Update: {status_text}",
#                 body=html_content,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[order.email],
#             )
#             email.content_subtype = "html"
#             email.send()

#             return Response({"message": f"Order status updated to {new_status}"}, status=200)
#         except Order.DoesNotExist:
#             return Response({"error": "Order not found."}, status=404)

from dateutil.relativedelta import relativedelta

class UpdateOrderStatusView(APIView):
    def post(self, request, order_id):
        from .models import MonthlyBox

        new_status = request.data.get("status")
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response({"error": "Invalid status."}, status=400)

        try:
            order = Order.objects.get(id=order_id)
            order.status = new_status

            # ✅ If delivered, increment & schedule next
            if new_status == 'delivered':
                order.total_treats_delivered += 2
                order.total_toys_delivered += 3
                order.save()

                # Schedule next order
                next_date = order.created_at.date() + relativedelta(months=1)
                today = date.today()

                try:
                    next_box = MonthlyBox.objects.get(month=today.month, year=today.year)
                except MonthlyBox.DoesNotExist:
                    next_box = None

                Order.objects.create(
                    user=order.user,
                    billing_type=order.billing_type,
                    selected_plan=order.selected_plan,
                    first_name=order.first_name,
                    last_name=order.last_name,
                    email=order.email,
                    address=order.address,
                    city=order.city,
                    state=order.state,
                    zip=order.zip,
                    use_shipping_as_billing=order.use_shipping_as_billing,
                    payment_method=order.payment_method,
                    status='confirmed',
                    monthly_box=next_box,
                    total_treats_delivered=order.total_treats_delivered,
                    total_toys_delivered=order.total_toys_delivered,
                    created_at=next_date,
                )

            else:
                order.save()

            return Response({"message": f"Order status updated to {new_status}"}, status=200)

        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=404)





from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderBoxHistorySerializer

class UserBoxHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).select_related("monthly_box").order_by("-created_at")
        serializer = OrderBoxHistorySerializer(orders, many=True)
        return Response(serializer.data)



from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderRatingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_box(request, box_id):
    try:
        order = Order.objects.get(id=box_id, user=request.user)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=404)

    serializer = OrderRatingSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Rating updated.'})
    return Response(serializer.errors, status=400)



class RateBoxView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            box = order.monthly_box
            if not box:
                return Response({"error": "Box not found for this order."}, status=404)

            rating = request.data.get('rating')
            if not isinstance(rating, int) or not (1 <= rating <= 5):
                return Response({"error": "Rating must be an integer between 1 and 5."}, status=400)

            # ✅ Update order's rating
            order.rating = rating
            order.save()

            # ✅ Recalculate MonthlyBox rating from all linked orders
            related_orders = box.orders.exclude(rating=0)
            total_ratings = related_orders.count()
            rating_sum = sum(o.rating for o in related_orders)
            box.rating = round(rating_sum / total_ratings, 1)
            box.total_ratings = total_ratings
            box.rating_sum = rating_sum
            box.save()

            return Response({"message": "Thanks for rating!"}, status=200)

        except Order.DoesNotExist:
            return Response({"error": "Order not found or not yours."}, status=404)






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from datetime import timedelta


# class CurrentSubscriptionView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         order = Order.objects.filter(user=request.user).order_by('-created_at').first()
#         if not order:
#             return Response({'detail': 'No subscription found'}, status=404)

#         # Estimate next billing date and ship date
#         created = order.created_at.date()
#         next_billing = created.replace(day=15)
#         if created.day > 15:
#             next_billing = (created.replace(day=28) + timedelta(days=7)).replace(day=15)
#         ship_date = next_billing - timedelta(days=5)

#         data = {
#             "plan": order.get_selected_plan_display(),
#             "price": "$27/month",  # optionally store dynamically later
#             "next_billing": next_billing.strftime("%B %d, %Y"),
#             "ship_date": ship_date.strftime("%B %d"),
#             "dog_size": request.user.dog.get_size_display() if hasattr(request.user, 'dog') else "N/A",
#             "box_theme": order.monthly_box.name if order.monthly_box else "",
#             "box_month": order.monthly_box.month if order.monthly_box else None,
#             "box_year": order.monthly_box.year if order.monthly_box else None,
#             "box_image": order.monthly_box.image.url if order.monthly_box and order.monthly_box.image else None,
#         }
#         return Response(data)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, OrderSerializer, UserProfileSerializer, DogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Order
from datetime import date
from django.contrib.auth import get_user_model




class SignupWithDogView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()

            user_email = result["user"]["email"]
            user_name = user_email.split("@")[0].capitalize()

            html_content = f"""
                <div style="font-family:Arial,sans-serif;padding:20px;background:#f9f9f9;">
                    <h2 style="color:#4CAF50;">Welcome to BarkBox, {user_name}!</h2>
                    <p>Thanks for signing up. We’re excited to send goodies your dog will love 🐶</p>
                    <p>Explore your dashboard and update your preferences anytime.</p>
                    <p style="margin-top:30px;">Cheers,<br/>The BarkBox Team</p>
                </div>
            """

            try:
                email = EmailMessage(
                    subject="🎉 Welcome to BarkBox!",
                    body=html_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[user_email],
                )
                email.content_subtype = "html"
                email.send()
            except Exception as e:
                print(f"❌ Failed to send welcome email: {e}")

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class OrderCheckoutView(APIView):
#     def post(self, request):
#         from .models import MonthlyBox
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             today = date.today()
#             try:
#                 box = MonthlyBox.objects.get(month=today.month, year=today.year)
#             except MonthlyBox.DoesNotExist:
#                 return Response({'error': 'No MonthlyBox defined for this month'}, status=400)

#             order = serializer.save()
#             order.monthly_box = box
#             order.save()

#             return Response({'order_id': order.id, 'message': 'Order placed successfully'}, status=201)
#         return Response(serializer.errors, status=400)

from datetime import timedelta
from dateutil.relativedelta import relativedelta 
User = get_user_model()

class OrderCheckoutView(APIView):
    def post(self, request):
        from .models import MonthlyBox
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.validated_data['email']).first()
            if not user:
                return Response({'error': 'User not found'}, status=404)

            # First box date logic (1 month after signup)
            first_box_date = user.date_joined.date() + relativedelta(months=1)
            today = date.today()

            try:
                box = MonthlyBox.objects.get(month=today.month, year=today.year)
            except MonthlyBox.DoesNotExist:
                return Response({'error': 'No MonthlyBox defined for this month'}, status=400)

            order = serializer.save()
            order.monthly_box = box
            order.total_treats_delivered = 2
            order.total_toys_delivered = 3
            order.created_at = first_box_date  # delay order creation to match first delivery logic
            order.save()

            return Response({'order_id': order.id, 'message': 'Order placed successfully'}, status=201)

        return Response(serializer.errors, status=400)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dog = getattr(request.user, "dog", None)
        if dog:
            serializer = DogSerializer(dog)
            return Response(serializer.data)
        return Response({"detail": "Dog profile not found."}, status=404)

    def put(self, request):
        dog = getattr(request.user, "dog", None)
        if not dog:
            return Response({"detail": "Dog profile not found."}, status=404)
        serializer = DogSerializer(dog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SendEmailAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        to_email = request.data.get('to')
        subject = request.data.get('subject')
        html_content = request.data.get('html')

        print("📩 Email Request Received:")
        print("To:", to_email)
        print("Subject:", subject)
        print("HTML snippet:", html_content[:100])

        if not all([to_email, subject, html_content]):
            return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            email = EmailMessage(
                subject,
                html_content,
                settings.DEFAULT_FROM_EMAIL,
                [to_email],
            )
            email.content_subtype = "html"
            email.send()
            return Response({'message': 'Email sent'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class UpdateOrderStatusView(APIView):
#     def post(self, request, order_id):
#         new_status = request.data.get("status")

#         if new_status not in dict(Order.STATUS_CHOICES):
#             return Response({"error": "Invalid status."}, status=400)

#         try:
#             order = Order.objects.get(id=order_id)
#             order.status = new_status
#             order.save()

#             status_text = new_status.replace('_', ' ').title()

#             html_content = f"""
#                 <div style="font-family: Arial, sans-serif; background: #f9f9f9; padding: 30px; border-radius: 10px; max-width: 600px; margin: auto; color: #333;">
#                   <h2 style="color: #4CAF50;">🐾 Hi {order.first_name},</h2>

#                   <p style="font-size: 16px;">
#                     We wanted to give you a quick update — your BarkBox order is now marked as:
#                     <strong style="color: #4CAF50;">{status_text}</strong> 🎉
#                   </p>

#                   <p style="font-size: 16px;">
#                     Our team is preparing everything to ensure your pup gets the best treats, toys, and tail-wagging joy 💌.
#                   </p>

#                   <div style="background: #fff; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 0 8px rgba(0,0,0,0.05);">
#                     <h3 style="margin-bottom: 10px;">📦 Order Details:</h3>
#                     <ul style="padding-left: 20px; font-size: 15px;">
#                       <li><strong>Plan:</strong> {order.get_selected_plan_display()}</li>
#                       <li><strong>Shipping To:</strong> {order.address}, {order.city}, {order.state}, {order.zip}</li>
#                       <li><strong>Status:</strong> {status_text}</li>
#                     </ul>
#                   </div>

#                   <p style="font-size: 15px;">Stay tuned — we’ll keep you posted on every step until your box arrives at your doorstep 🐶📬</p>

#                   <p style="margin-top: 30px; font-size: 15px;">
#                     Woofs & Wags,<br/>
#                     <strong>The BarkBox Team</strong> 💙
#                   </p>
#                 </div>
#             """

#             email = EmailMessage(
#                 subject=f"📦 BarkBox Order Update: {status_text}",
#                 body=html_content,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[order.email],
#             )
#             email.content_subtype = "html"
#             email.send()

#             return Response({"message": f"Order status updated to {new_status}"}, status=200)
#         except Order.DoesNotExist:
#             return Response({"error": "Order not found."}, status=404)

from dateutil.relativedelta import relativedelta

class UpdateOrderStatusView(APIView):
    def post(self, request, order_id):
        from .models import MonthlyBox

        new_status = request.data.get("status")
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response({"error": "Invalid status."}, status=400)

        try:
            order = Order.objects.get(id=order_id)
            order.status = new_status


            if new_status == 'delivered':
                order.total_treats_delivered += 2
                order.total_toys_delivered += 3
                order.save()

                # Schedule next order
                next_date = order.created_at.date() + relativedelta(months=1)
                today = date.today()

                try:
                    next_box = MonthlyBox.objects.get(month=today.month, year=today.year)
                except MonthlyBox.DoesNotExist:
                    next_box = None

                Order.objects.create(
                    user=order.user,
                    billing_type=order.billing_type,
                    selected_plan=order.selected_plan,
                    first_name=order.first_name,
                    last_name=order.last_name,
                    email=order.email,
                    address=order.address,
                    city=order.city,
                    state=order.state,
                    zip=order.zip,
                    use_shipping_as_billing=order.use_shipping_as_billing,
                    payment_method=order.payment_method,
                    status='confirmed',
                    monthly_box=next_box,
                    total_treats_delivered=order.total_treats_delivered,
                    total_toys_delivered=order.total_toys_delivered,
                    created_at=next_date,
                )

            else:
                order.save()

            return Response({"message": f"Order status updated to {new_status}"}, status=200)

        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=404)





from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderBoxHistorySerializer

class UserBoxHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).select_related("monthly_box").order_by("-created_at")
        serializer = OrderBoxHistorySerializer(orders, many=True)
        return Response(serializer.data)



from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderRatingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_box(request, box_id):
    try:
        order = Order.objects.get(id=box_id, user=request.user)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=404)

    serializer = OrderRatingSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Rating updated.'})
    return Response(serializer.errors, status=400)



class RateBoxView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            box = order.monthly_box
            if not box:
                return Response({"error": "Box not found for this order."}, status=404)

            rating = request.data.get('rating')
            if not isinstance(rating, int) or not (1 <= rating <= 5):
                return Response({"error": "Rating must be an integer between 1 and 5."}, status=400)

            # ✅ Update order's rating
            order.rating = rating
            order.save()

            # ✅ Recalculate MonthlyBox rating from all linked orders
            related_orders = box.orders.exclude(rating=0)
            total_ratings = related_orders.count()
            rating_sum = sum(o.rating for o in related_orders)
            box.rating = round(rating_sum / total_ratings, 1)
            box.total_ratings = total_ratings
            box.rating_sum = rating_sum
            box.save()

            return Response({"message": "Thanks for rating!"}, status=200)

        except Order.DoesNotExist:
            return Response({"error": "Order not found or not yours."}, status=404)






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from datetime import timedelta


# class CurrentSubscriptionView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         order = Order.objects.filter(user=request.user).order_by('-created_at').first()
#         if not order:
#             return Response({'detail': 'No subscription found'}, status=404)

#         # Estimate next billing date and ship date
#         created = order.created_at.date()
#         next_billing = created.replace(day=15)
#         if created.day > 15:
#             next_billing = (created.replace(day=28) + timedelta(days=7)).replace(day=15)
#         ship_date = next_billing - timedelta(days=5)

#         data = {
#             "plan": order.get_selected_plan_display(),
#             "price": "$27/month",  # optionally store dynamically later
#             "next_billing": next_billing.strftime("%B %d, %Y"),
#             "ship_date": ship_date.strftime("%B %d"),
#             "dog_size": request.user.dog.get_size_display() if hasattr(request.user, 'dog') else "N/A",
#             "box_theme": order.monthly_box.name if order.monthly_box else "",
#             "box_month": order.monthly_box.month if order.monthly_box else None,
#             "box_year": order.monthly_box.year if order.monthly_box else None,
#             "box_image": order.monthly_box.image.url if order.monthly_box and order.monthly_box.image else None,
#         }
#         return Response(data)

from calendar import month_name
from datetime import timedelta, date
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, MonthlyBox

# class CurrentSubscriptionView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         order = Order.objects.filter(user=request.user).order_by('-created_at').first()
#         if not order:
#             return Response({'detail': 'No subscription found'}, status=404)

#         # Estimate next billing and ship date
#         created = order.created_at.date()
#         next_billing = created.replace(day=15)
#         if created.day > 15:
#             next_billing = (created.replace(day=28) + timedelta(days=7)).replace(day=15)
#         ship_date = next_billing - timedelta(days=5)

#         # Lookup next box
#         next_box = MonthlyBox.objects.filter(
#             year=next_billing.year,
#             month=next_billing.month
#         ).first()

#         # Aggregate delivery stats
#         all_orders = Order.objects.filter(user=request.user)
#         total_boxes_delivered = all_orders.filter(status="delivered").count()
#         total_treats = sum(o.total_treats_delivered for o in all_orders)
#         total_toys = sum(o.total_toys_delivered for o in all_orders)

#         data = {
#             "plan": order.get_selected_plan_display(),
#             "price": "$27/month",
#             "next_billing": next_billing.strftime("%B %d, %Y"),
#             "ship_date": ship_date.strftime("%B %d"),
#             "dog_size": request.user.dog.get_size_display() if hasattr(request.user, 'dog') else "N/A",
#             "total_boxes_delivered": total_boxes_delivered,
#             "total_treats_delivered": total_treats,
#             "total_toys_delivered": total_toys,
#             "next_box": {
#                 "theme": next_box.name if next_box else None,
#                 "month_name": month_name[next_billing.month],
#                 "year": next_billing.year,
#                 "ship_date": ship_date.strftime("%B %d, %Y"),
#                 "image": next_box.image_public_url if next_box else None
#             } if next_box else None
#         }

#         return Response(data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, MonthlyBox
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class CurrentSubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(user=request.user).order_by('-created_at').first()
        if not order:
            return Response({'detail': 'No subscription found'}, status=404)

        # Adjust next billing date based on skipped months
        skipped = order.skipped_months
        next_billing = order.created_at.date() + relativedelta(months=skipped + 1)  # Skip handling
        ship_date = next_billing - timedelta(days=5)

        # Fetch next and current box
        next_box = MonthlyBox.objects.filter(year=next_billing.year, month=next_billing.month).first()
        current_box = MonthlyBox.objects.filter(year=order.created_at.year, month=order.created_at.month).first()

        # Calculate remaining months based on the skipped months and selected plan
        plan_duration = int(order.selected_plan[:2])  # e.g., '6mo' -> 6
        remaining_months = plan_duration + order.skipped_months  # Add skipped months

        data = {
            "plan": order.get_selected_plan_display(),
            "remaining_months": remaining_months,
            "next_billing": next_billing.strftime("%B %d, %Y"),
            "ship_date": ship_date.strftime("%B %d"),
            "dog_size": request.user.dog.get_size_display() if hasattr(request.user, 'dog') else "N/A",
            "next_box": {
                "theme": next_box.name if next_box else None,
                "image": next_box.image_public_url if next_box else None
            } if next_box else None,
            "current_box": {
                "theme": current_box.name if current_box else None,
                "image": current_box.image_public_url if current_box else None
            } if current_box else None
        }
        return Response(data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from rest_framework import status

class SkipBoxView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = Order.objects.filter(user=request.user).first()
        
        if not order:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        # Increment skipped months
        order.skipped_months += 1
        order.save()

        # Calculate remaining months based on selected plan and skipped months
        plan_duration = int(order.selected_plan[:2])  # e.g., '6mo' -> 6
        remaining_months = plan_duration + order.skipped_months  # Add skipped months
        
        # Update plan duration dynamically (e.g., 6 months becomes 7 after skipping)
        order.selected_plan = f"{remaining_months}mo"
        order.save()

        # Return response with updated remaining months
        return Response({
            "message": "Next box skipped successfully.",
            "remaining_months": remaining_months  # Show updated remaining months after skip
        }, status=status.HTTP_200_OK)

