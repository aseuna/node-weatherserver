<template>
    <div id="findContainer">
        <b-form
        inline
        @submit.prevent
        >

            <b-form-group
            label="Aloitus pvm: "
            label-for="startDate"
            >
                <b-form-input
                id="startDate"
                required
                type="date"
                >
                </b-form-input>
            </b-form-group>

            <b-form-group
            label="Lopetus pvm: "
            label-for="endDate"
            >
                <b-form-input
                id="endDate"
                required
                type="date"
                >
                </b-form-input>
            </b-form-group>

        </b-form>
    </div>
</template>

<script>
export default {
    name: 'Find'
}
</script>

<style scoped>

</style>