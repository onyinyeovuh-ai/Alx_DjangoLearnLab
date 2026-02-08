# Managing Permissions and Groups in Django

## Overview
This project implements role-based access control using Django groups and custom permissions
to restrict access to different parts of the application.

## Custom Permissions
Custom permissions were added to the Book model in the `bookshelf` app using `Meta.permissions`:

- can_view
- can_create
- can_edit
- can_delete

These permissions are created automatically when migrations are applied.

## Groups Configuration
The following groups were created using the Django admin panel:

### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

## Permission Enforcement in Views
Access to views is restricted using Django’s `@permission_required` decorator.
Users without the required permission receive a 403 Forbidden response.

## Testing
Test users were assigned to different groups and manually tested to confirm that
permissions are enforced correctly.