# class_models.py
from typing import TypedDict, Optional, List, Dict, Any

class AuthPayload(TypedDict):
    authenticated: bool
    reason : str
    user_id: Optional[str]
    ban_status: bool


class LoginCheckPayload(TypedDict):
    user_id: str
    password: str
    role: Optional[str]


class NLPAnalysisPayload(TypedDict):
    scope_tag: str
    issue_tags: List[str]
    priority: str


class ComplaintRecord(TypedDict):
    uid: str
    author_id: str
    title: str
    description: str
    scope_tag: str
    issue_tags: str          # JSON string, e.g. '["WATER_ISSUE"]'
    priority: str
    status: str              # "OPEN" or "CLOSED"
    initial_sub_count: int
    created_at: str
    has_unread_alert: int    # 0 or 1


class CommentRecord(TypedDict):
    comment_id: int
    complaint_uid: str
    author_id: str
    content: str
    is_solution: int         # 0 or 1
    upvotes: int
    downvotes: int
    created_at: str


class VoteResultPayload(TypedDict):
    success: bool
    reopened: bool
    msg: str


class AuditLogRecord(TypedDict):
    log_id: int
    complaint_uid: str
    actor_id: str
    action_type: str
    details: str
    timestamp: str


class SessionStateKeys(TypedDict):
    logged_in: bool
    user_id: Optional[str]
    role: Optional[str]
    current_view: str        # "RAISE", "LOOK", "MY_COMPLAINTS", "THREAD_DETAIL"
    selected_uid: Optional[str]
    draft_analysis: Optional[Dict[str, Any]]
