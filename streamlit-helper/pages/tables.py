import streamlit as st
import pandas as pd
import numpy as np

def show():
    st.title(f"Streamlit Table Functionality")

    st.header("Dataframe Table")
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df)  # Same as st.write(df)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
            import numpy as np
                                
            st.header("Dataframe Table")
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)  # Same as st.write(df)      
            ```
            """)
    
    st.header("Static Table")
    st.table(df)
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
            import numpy as np

            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))     
            st.table(df)      
            ```
            """)

    
    st.header("Editor Table")
    df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
    )
    edited_df = st.data_editor(df)
    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            import pandas as pd
                                
            st.header("Editor Table")
                df = pd.DataFrame(
                [
                {"command": "st.selectbox", "rating": 4, "is_widget": True},
                {"command": "st.balloons", "rating": 5, "is_widget": False},
                {"command": "st.time_input", "rating": 3, "is_widget": True},
            ]
            )
            edited_df = st.data_editor(df)

            favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
            st.markdown(f"Your favorite command is **{favorite_command}** 🎈")      
            ```
            """)
        
    st.link_button("Column Configuration Capabilities", "https://docs.streamlit.io/library/api-reference/data/st.column_config")

    st.header("Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st

            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", "70 °F", "1.2 °F")
            col2.metric("Wind", "9 mph", "-8%")
            col3.metric("Humidity", "86%", "4%")      
            ```
            """)

    st.header("Json Entries")
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st

            st.json({
                'foo': 'bar',
                'baz': 'boz',
                'stuff': [
                    'stuff 1',
                    'stuff 2',
                    'stuff 3',
                    'stuff 5',
                ],
            })     
            ```
            """)


