"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name', validators=[InputRequired()])
    description = TextAreaField('Playlist Description')
    submit = SubmitField('Add Playlist')


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired()])
    artist = StringField('Artist', validators=[InputRequired()])
    submit = SubmitField('Add Song')


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
