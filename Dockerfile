FROM netboxcommunity/netbox:v4.5.3

COPY ./plugin_requirements.txt /opt/netbox/
RUN /usr/local/bin/uv pip install -r /opt/netbox/plugin_requirements.txt

COPY ./configuration.py /etc/netbox/config/configuration.py
COPY ./extra.py /etc/netbox/config/extra.py
COPY ./plugins.py /etc/netbox/config/plugins.py
RUN DEBUG="true" SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy" \
    /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input

RUN echo "# extra.py" > /etc/netbox/config/extra.py
RUN echo "# plugins.py" > /etc/netbox/config/plugins.py
