Permissions & Groups Setup:
- Custom permissions are defined in Book.Meta:
    can_view, can_create, can_edit, can_delete
- Groups:
    Viewers → can_view
    Editors → can_view, can_create, can_edit
    Admins → all permissions
- Views are protected using @permission_required with matching codenames.
