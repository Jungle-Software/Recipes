import { gql, useMutation } from "@apollo/client";
import { Modal } from "react-bootstrap";
import DevError from "../../../components/DevError/DevError";
import { Button } from "./AddRecipeDialog.styles";

// TODO implement this
export const ADD_RECIPE_MUTATION = gql`
    mutation AddRecipe {
            addRecipe {
                recipe {
                id
            }
        }
    }
`;

type Props = {
    show: boolean
    hide: Function
    handleSubmit: Function
}

const AddRecipeDialog = (props: Props) => {
    const [addRecipe, { data, loading, error }] = useMutation(ADD_RECIPE_MUTATION, {
        variables: { /*  */ },
        onCompleted() {
            props.handleSubmit()
        },
        onError() {}
      });

    if (loading) return <div>Adding...</div>;
    if (error) return <DevError message={error.message}></DevError>; 
    if (data) return <div>Added!</div> // TODO maybe show a snackbar or something on fail/success (part of UI task)

    return (
        <Modal show={props.show} onHide={() => {props.hide()}}>
            {/* TODO do we want a static backdrop or no? (prevents from clicking outside) https://react-bootstrap.github.io/components/modal/*/}
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>

            <Button 
                onClick={() => {addRecipe()}}
                id="submit-button"
            >Submit</Button>
        </Modal>
      )
}

export default AddRecipeDialog;