from datetime import datetime

from pydantic import BaseModel


class UserMinimal(BaseModel):
    id: int
    username: str
    name: str
    avatar_template: str


class Topic(BaseModel):
    tags: list[str | None]
    tags_descriptions: dict[str, str]
    id: int
    title: str
    fancy_title: str
    posts_count: int
    created_at: datetime
    views: int
    reply_count: int
    like_count: int
    last_posted_at: datetime
    visible: bool
    closed: bool
    archived: bool
    archetype: str
    slug: str
    category_id: int
    word_count: int
    deleted_at: datetime | None
    user_id: int
    featured_link: str | None
    pinned_globally: bool
    pinned_at: datetime | None
    pinned_until: datetime | None
    unpinned: str | None
    pinned: bool
    highest_post_number: int
    deleted_by: str | None
    has_deleted: bool
    bookmarked: bool
    participant_count: int
    thumbnails: str | None
    created_by: UserMinimal
    last_poster: UserMinimal
    tags_disable_ads: bool


class InNewPost(BaseModel):
    topic: Topic
