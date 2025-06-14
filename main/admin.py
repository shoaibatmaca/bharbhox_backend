# from django.contrib import admin
# from .models import *
# from django.core.mail import EmailMessage
# from django.conf import settings



# admin.site.register(Dog)
# admin.site.register(MonthlyBox)


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'status', 'created_at']
#     list_filter = ['status']

#     def save_model(self, request, obj, form, change):
#         old_status = obj.__class__.objects.get(pk=obj.pk).status if obj.pk else None
#         super().save_model(request, obj, form, change)

#         # Check if status changed
#         if change and old_status != obj.status:
#             self.send_status_email(obj)

#     def send_status_email(self, order):
#         status_text = order.status.replace('_', ' ').title()
#         subject = f"📦 BarkBox Order Update: {status_text}"

#         body = f"""
# <div style="font-family: Arial, sans-serif; background: #f9f9f9; padding: 30px; border-radius: 10px; max-width: 600px; margin: auto; color: #333;">
#   <h2 style="color: #4CAF50;">🐾 Hi {order.first_name},</h2>

#   <p style="font-size: 16px;">
#     We wanted to give you a quick update — your BarkBox order is now marked as:
#     <strong style="color: #4CAF50;">{status_text}</strong> 🎉
#   </p>

#   <p style="font-size: 16px;">
#     Our team is preparing everything to ensure your pup gets the best treats, toys, and tail-wagging joy 💌.
#   </p>

#   <div style="background: #fff; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 0 8px rgba(0,0,0,0.05);">
#     <h3 style="margin-bottom: 10px;">📦 Order Details:</h3>
#     <ul style="padding-left: 20px; font-size: 15px;">
#       <li><strong>Plan:</strong> {order.get_selected_plan_display()}</li>
#       <li><strong>Shipping To:</strong> {order.address}, {order.city}, {order.state}, {order.zip}</li>
#       <li><strong>Status:</strong> {status_text}</li>
#     </ul>
#   </div>

#   <p style="font-size: 15px;">Stay tuned — we’ll keep you posted on every step until your box arrives at your doorstep 🐶📬</p>

#   <p style="margin-top: 30px; font-size: 15px;">
#     Woofs & Wags,<br/>
#     <strong>The BarkBox Team</strong> 💙
#   </p>
# </div>
# """

#         try:
#             email = EmailMessage(
#                 subject=subject,
#                 body=body,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[order.email],
#             )
#             email.content_subtype = "html"  # 💡 this tells Django it's HTML
#             email.send()
#             print("✅ Email sent from admin status update")
#         except Exception as e:
#             print("❌ Failed to send admin email:", e)

from django.contrib import admin
from .models import Dog, MonthlyBox, Order
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta


admin.site.register(Dog)
admin.site.register(MonthlyBox)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'total_treats_delivered', 'total_toys_delivered']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        old_status = obj.__class__.objects.get(pk=obj.pk).status if obj.pk else None
        super().save_model(request, obj, form, change)

        # Send email if status changed
        if change and old_status != obj.status:
            self.send_status_email(obj)

            # If order was just marked as delivered, update counters & create next order
            if obj.status == 'delivered':
                self.handle_box_delivery(obj)

    def send_status_email(self, order):
        status_text = order.status.replace('_', ' ').title()
        subject = f"📦 BarkBox Order Update: {status_text}"

        body = f"""
<div style="font-family: Arial, sans-serif; background: #f9f9f9; padding: 30px; border-radius: 10px; max-width: 600px; margin: auto; color: #333;">
  <h2 style="color: #4CAF50;">🐾 Hi {order.first_name},</h2>

  <p style="font-size: 16px;">
    We wanted to give you a quick update — your BarkBox order is now marked as:
    <strong style="color: #4CAF50;">{status_text}</strong> 🎉
  </p>

  <p style="font-size: 16px;">
    Our team is preparing everything to ensure your pup gets the best treats, toys, and tail-wagging joy 💌.
  </p>

  <div style="background: #fff; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 0 8px rgba(0,0,0,0.05);">
    <h3 style="margin-bottom: 10px;">📦 Order Details:</h3>
    <ul style="padding-left: 20px; font-size: 15px;">
      <li><strong>Plan:</strong> {order.get_selected_plan_display()}</li>
      <li><strong>Shipping To:</strong> {order.address}, {order.city}, {order.state}, {order.zip}</li>
      <li><strong>Status:</strong> {status_text}</li>
    </ul>
  </div>

  <p style="font-size: 15px;">Stay tuned — we’ll keep you posted on every step until your box arrives at your doorstep 🐶📬</p>

  <p style="margin-top: 30px; font-size: 15px;">
    Woofs & Wags,<br/>
    <strong>The BarkBox Team</strong> 💙
  </p>
</div>
"""

        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[order.email],
            )
            email.content_subtype = "html"
            email.send()
            print("✅ Email sent from admin status update")
        except Exception as e:
            print("❌ Failed to send admin email:", e)

    def handle_box_delivery(self, order):
        from .models import Order, MonthlyBox

        # Increment treats/toys
        order.total_treats_delivered += 2
        order.total_toys_delivered += 3
        order.save()

        # Calculate next delivery date
        next_delivery_date = order.created_at + relativedelta(months=1)
        try:
            next_box = MonthlyBox.objects.get(month=now().month, year=now().year)
        except MonthlyBox.DoesNotExist:
            next_box = None

        # Schedule next order
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
            monthly_box=next_box,
            use_shipping_as_billing=order.use_shipping_as_billing,
            status='confirmed',
            payment_method=order.payment_method,
            total_treats_delivered=order.total_treats_delivered,
            total_toys_delivered=order.total_toys_delivered,
            created_at=next_delivery_date,
        )
