import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show():
    st.title(f"Streamlit Graphs Functionality")

    st.link_button("Click here for more complex Graphs & Charts", 'https://docs.streamlit.io/library/api-reference/charts')

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.header("Area Chart")
    st.area_chart(chart_data)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
                    
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.header("Area Chart")
            st.area_chart(chart_data)        
            ```
            """)
        
    st.header("Bar Chart")
    st.bar_chart(chart_data)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
                    
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.header("Bar Chart")
            st.bar_chart(chart_data)       
            ```
            """)
        
    st.header("Line Chart")
    st.line_chart(chart_data)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
                    
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.header("Line Chart")
            st.line_chart(chart_data)        
            ```
            """)
        
    st.header("Scatter Chart")
    st.scatter_chart(chart_data)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
                    
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.header("Scatter Chart")
            st.scatter_chart(chart_data)        
            ```
            """)

    map_df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
    st.header("Map Graph")
    st.map(map_df)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
                    
            map_df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
            st.header("Map Graph")
            st.map(map_df)        
            ```
            """)

    c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )
    st.header("Altair Chart")
    st.altair_chart(c, use_container_width=True)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import altair as alt
                    
            c = (
                alt.Chart(chart_data)
                .mark_circle()
                .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
                )

                st.header("Altair Chart")
                st.altair_chart(c, use_container_width=True)       
            ```
            """)

    st.header("Vega Lite Chart")
    st.vega_lite_chart(
        chart_data,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "a", "type": "quantitative"},
                "y": {"field": "b", "type": "quantitative"},
                "size": {"field": "c", "type": "quantitative"},
                "color": {"field": "c", "type": "quantitative"},
            },
        },
        )
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import altair as alt
                    
            st.header("Vega Lite Chart")
            st.vega_lite_chart(
                chart_data,
                {
                    "mark": {"type": "circle", "tooltip": True},
                    "encoding": {
                        "x": {"field": "a", "type": "quantitative"},
                        "y": {"field": "b", "type": "quantitative"},
                        "size": {"field": "c", "type": "quantitative"},
                        "color": {"field": "c", "type": "quantitative"},
                    },
                },
                )
            ```
            """)